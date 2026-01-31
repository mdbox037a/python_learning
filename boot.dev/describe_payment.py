from dataclasses import dataclass


@dataclass
class PaymentSuccess:
    amount: int
    currency: str


@dataclass
class PaymentDeclined:
    reason: str


@dataclass
class PaymentError:
    code: int
    message: str


def describe_payment(result):
    match result:
        case PaymentSuccess(amount=amount, currency=currency):
            return f"Payment of {amount} {currency} succeeded"
        case PaymentDeclined(reason=reason):
            return f"Payment declined: {reason}"
        # BUG: this case matches *all* PaymentError variants first,
        # so the more specific logic is never reached
        case PaymentError(code=code, message=message):
            return f"Temporary payment error (code {code}): {message}"
        case PaymentError(code=code, message=message) if code < 500:
            return f"Permanent payment error (code {code}): {message}"
        case _:
            raise ValueError("Unknown payment result type")

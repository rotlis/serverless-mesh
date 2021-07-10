"""
First lambda
"""

def lambda_function(event, context):
    """
    entry point of lambda
    """
    print("event: ", event)
    print("context: ", context)
    return "ok"

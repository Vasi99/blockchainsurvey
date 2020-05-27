import hashlib

user_1 = "mock_username"
user_2 = "mock_user"

mock_question_1 = "What is your age?"
mock_question_2 = "How is the weather?"

mock_response_1 = "It is very humid here. Need to run the AC all the time."
mock_response_2 = "Great!"

unknown_user_1 = hashlib.sha256(b"public_key_of_some_user").hexdigest()
unknown_user_2 = hashlib.sha256(b"public_key_of_some_other_user").hexdigest()
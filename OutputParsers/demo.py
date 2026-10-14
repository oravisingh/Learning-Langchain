# No all LLMs can give you structured output by their own like you can't use with_structured_output and get a structured otuput
# So there comes Output Parsers
# They can b eused with both the types of models 1. structured_output Generatable and 2. structured_output UnGeneratable
# Output Parsers in LangChain help convert raw LLm responses into structured formats like JSON, CSv, Pydantic models and more.They ensure consistency, validating, and ease of use in applications.
# Four Types of output Parsers

# 1. String O/P
# 2. JSON O/P
# 3. Structured O/P
# 4. Pydantic O/P
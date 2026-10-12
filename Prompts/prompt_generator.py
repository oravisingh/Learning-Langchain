from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper_title", "style", "length"],
    template="""
        You are a research assistant.
        Write a {style} of the paper titled "{paper_title}".
        Keep the response {length} in length.
        Focus on the main ideas, significance, methods, and key takeaways.
        Present it in clear, professional English.
        1.Mathemaitcal Formula:
            -Use the mathematical formula(if any) as well to explain in a simple manner.
        2.Analogy:
            -Use analogy to explain the concept in a simple manner. 
        """,
    validate_template=True, # Used to validate the template and ensure that all required input variables are provided.

    )

template.save("Prompts/prompt_generator.json")
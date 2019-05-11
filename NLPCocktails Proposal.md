# NLPCocktails

This project I think I'm going to build a database of cocktails and a web app thing that can parse a plain language search and invent a cocktail to match it

You sidle up at a schnazzy speakeasy downtown and bartender asks you what you're feeling like. "Oooh,"you say…"can you give me something that's…crisp? And smoky, but not too boozy. More like…I wanna feel it, you know? Oh, but no vodka, I hate that stuff"

"I know just the thing," the bartender says. You see him get to work grabbing one bottle after another of things you've never heard of before, and a moment later you've got a bit of magic in your mouth, somehow exactly what you'd just asked for. 

That kind of bartender is a special find, a true mixologist, But can we get that kind of thing in the comfort of our own home?

## The Natural Language Purveyor of Cocktails

Using an algorithm that integrates knowledge of all sorts liquors and ingredients, recipes and descriptions for thousands of cocktail recipes , and a powerful engine for processing and interpreting natural language, NLPCocktails can interpret a plain English request and provide a cocktail matching the request—perhaps even inventing a new one just for you.





Hmm...I wonder if I could construct two feature spaces, one some l x n matrix of descriptions of cocktails parsed and processed by some NLP trickery and the other an m x n matrix of all the potential ingredients with quantities as values. Then come up with a transform function that reduces the dimensionality of the description matrix (I expect l > m ) to match the ingredient matrix...and what I'm wondering how I could align the transformation such that 
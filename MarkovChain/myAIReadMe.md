### 11/1/2024

## AI_ 


## Markov Chain generator

- The Markov Chain is a mathematical model used to represent a sequence of events, where the probability of each event depends only on the state attained from the previous event, not on the sequence of events that preceded it. This property is known as "memory lessness."<br>

## System States
Imagine you have four possible states that the system can be in:<br>

`State A`<br>
`State B`<br>
`State C`<br>
`State D`<br>

- Each state has a certain probability of transitioning to another state. Rather than thinking of each state as having an independent probability of occurring, think of it in terms of `transition probabilities`. These probabilities determine the likelihood of moving from one state to another.<br>

## Transition Probabilities

The probabilities of transitioning between states can be represented in a transition matrix. For example, if we assign probabilities to moving from one state to another:<br>

- If the system is in `State A`, it might have:<br>
<br>
- A 32% chance of transitioning to `State B`
- A 32% chance of transitioning to `State C`
- A 32% chance of transitioning to `State D`
- A 4% chance of remaining in `State A`
<br>
The probabilities for each state should sum to 100% or 1 in decimal form.

## Understanding How the Markov Chain Works

In a Markov Chain, we only care about the current state and the probabilities of moving to other states. We do not account for the sequence of states that led to the current state.

### Transitional Probabilities

`States`

- When the system is in `State A`, it will transition to `State B`, `State C`, or `State D` with the given probabilities.<br>
- If the system is in `State B`, it will have its own set of transition probabilities, determining where it will go next.<br>
- The process continues, and each transition depends solely on the current state, not on how the system arrived at that state.<br>


## Why the wall of text Markov regarding the `markovChain.py` script? 

The Markov Chain generator is designed to model text sequences based on the probabilities of words or phrases following each other. Considering my sources:<br>

- Food Service Documentation - AR30-22
- Index of recipe cards

### Receiving and Cleaning Content:

The generator first extracts the raw text from PDF files using the `pdfminer` library. This `raw_text` is then cleaned to remove unwanted characters, headers, footers, and other non-essential content.<br>
<br>
Cleaning the content helps ensure that the text used for building the model is more coherent and free from irrelevant noise, but it doesn't change the overall distribution or structure of the content's vocabulary.<br>

### Processing Content:

The generator splits the cleaned text into words and creates a model where each word sequence of a given size `state_size` is mapped to the words that follow it.<br>

`state_size`: With a `state_size` of 2, the generator looks at two-word sequences or "states" and records which words come next.<br>
For example, if the text contains "Army installation procedures," it will note that "procedures" can follow "Army installation."<br>

The Markov model then builds a probabilistic mapping where each two-word sequence points to a list of possible words that can follow.<br>

### Generating Text:

The generator uses the model to create a new sequence of words. It starts with a random two-word sequence (that typically starts with a capital letter) and then repeatedly selects the next word based on the probabilities in the model.<br>
The generated text is not a summary. Instead, it is a stochastic reconstruction that resembles the original content in vocabulary and phrasing but does not convey a cohesive summary or specific meaning.<br>

- Stochastic: This term refers to a process that is random or involves some level of randomness. In mathematics, probability, or machine learning, stochastic methods rely on random variables or probabilities.<br>
- Reconstruction: This refers to rebuilding or regenerating something, often aiming to replicate or approximate a specific structure, pattern, or dataset.<br>

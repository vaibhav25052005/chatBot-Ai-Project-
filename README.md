Project Description: Simple Rule-Based Chatbot using Python

This project involves the development of a simple rule-based chatbot using the Python programming language. The chatbot interacts with users through a text-based interface and provides predefined responses based on specific keywords detected in the user’s input.

The chatbot works by converting user input into lowercase text and applying a series of conditional rules to identify common intents such as greetings, asking about the chatbot, inquiries about its name, well-being questions, and exit commands. If the user input matches any predefined rule, the chatbot responds with an appropriate message. If no rule matches, a default response is returned, prompting the user to rephrase their query.

The system runs in a continuous loop, allowing real-time interaction until the user types a termination command (bye). This project demonstrates fundamental concepts of string processing, conditional statements, functions, and loop control in Python, as well as an introduction to basic conversational AI logic.

Although simple in design, this chatbot serves as a foundation for understanding how conversational systems work and can be extended in the future using advanced techniques such as Natural Language Processing (NLP) or Machine Learning.

Key Features:

Rule-based intent recognition

Interactive command-line interface

Predefined responses for common user queries

Simple and beginner-friendly implementation

This project is ideal for beginners learning Python and exploring the basics of chatbot development. 

ChatBot

If you want, I can also:

Shorten this for a resume

Rewrite it for internship / college submission

Add future scope or objectives section-

### **1. Function Definition**

```python
def chatbot_response(user_input):
```

This function takes the user’s input and returns a chatbot reply based on rules.

---

### **2. Convert Input to Lowercase**

```python
user_input = user_input.lower()
```

This ensures the chatbot matches words like *Hi*, *HI*, or *hi* correctly.

---

### **3. Greeting Rules**

```python
if "hello" in user_input or "hi" in user_input:
```

If the user types **hello** or **hi**, the chatbot responds with a greeting.

---

### **4. Identity Questions**

```python
elif "who are you" in user_input:
```

Responds when the user asks about the chatbot.

```python
elif "your name" in user_input:
```

Tells the chatbot’s name.

---

### **5. Well-being Question**

```python
elif "how are you" in user_input:
```

Replies politely when the user asks how the chatbot is doing.

---

### **6. Exit Condition**

```python
elif "bye" in user_input or "goodbye" in user_input:
```

Handles goodbye messages.

---

### **7. Default Response**

```python
else:
    return "Sorry, I did not understand that. Can you rephrase?"
```

Used when the input does not match any rule.

---

### **8. Main Chat Loop**

```python
while True:
```

Keeps the chatbot running continuously.

```python
user_input = input("You: ")
```

Takes user input.

```python
if user_input.lower() == "bye":
```

Stops the program when the user types **bye**.

---

### **9. Display Response**

```python
print("ChatBot:", response)
```

Prints the chatbot’s reply.

---

### **Summary**

This is a **rule-based chatbot** that uses conditional statements (`if-elif-else`) to respond to user messages. It demonstrates core Python concepts like functions, loops, and string handling. 


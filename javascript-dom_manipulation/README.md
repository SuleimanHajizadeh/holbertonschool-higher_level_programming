Here is the **English version** of your document:

---

# JavaScript – DOM Manipulation

<div align="right">
  <a href="README.md">🇬🇧 English</a>
</div>

![JavaScript DOM Manipulation Banner](JavaScript%20DOM%20manipulation.jpg)

## Description

This project explores the fundamentals of **DOM (Document Object Model) manipulation** in JavaScript. Through a series of practical exercises, you will learn how to dynamically interact with HTML elements, handle user events, and perform network requests using the **Fetch API**.

## Learning Objectives

By the end of this project, you should be able to explain, without assistance:

### General Concepts

* How to select HTML elements in JavaScript
* The differences between ID, class, and tag selectors
* How to modify the style of an HTML element
* How to get and update the content of an HTML element
* How to modify the DOM
* How to make a request using `XMLHttpRequest`
* How to make a request using the Fetch API
* How to listen to / bind DOM events
* How to listen to / bind user events

## Resources

* [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
* [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
* [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
* [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
* [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
* [CSS Diner – Learn selectors by playing](https://flukeout.github.io/)
* [DOM Scripting](https://en.wikipedia.org/wiki/Dynamic_HTML)
* [What went wrong? JavaScript troubleshooting](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

## Requirements

### General

* Allowed editors: All
* All files will be interpreted in **Google Chrome** (version 57.0 or later)
* All files must end with a new line
* Your code must follow **`semistandard`**
* You are **not allowed to use `var`**
* The HTML page must **not reload** for each action (DOM manipulation, value updates, data fetching, etc.)

## Project Structure

```
javascript-dom_manipulation/
├── 0-script.js          # Change header color
├── 1-script.js          # Change color on click
├── 2-script.js          # Add a CSS class
├── 3-script.js          # Toggle between two classes
├── 4-script.js          # Add an element to a list
├── 5-script.js          # Update text
├── 6-script.js          # Fetch API – Star Wars character
├── 7-script.js          # Fetch API – Star Wars movies
├── 8-script.js          # Fetch API – "Hello" translation
└── README.md
```

## Tasks

### 0. Color Me

**File:** `0-script.js`

JavaScript script that updates the text color of the `header` element to red (`#FF0000`) using `document.querySelector`.

### 1. Click and Turn Red

**File:** `1-script.js`

Script that updates the text color of the `header` element to red (`#FF0000`) when the user clicks on the element with the id `red_header`.

### 2. Add `.red` Class

**File:** `2-script.js`

Script that adds the class `red` to the `header` element when the user clicks on the element with the id `red_header`.

### 3. Toggle Classes

**File:** `3-script.js`

Script that toggles the class of the `header` element between `red` and `green` when the user clicks on the element with the id `toggle_header`.

### 4. List of Elements

**File:** `4-script.js`

Script that adds a `<li>Item</li>` element to a `ul` list with the class `my_list` when the user clicks on the element with the id `add_item`.

### 5. Change the Text

**File:** `5-script.js`

Script that updates the text of the `header` element to **"New Header!!!"** when the user clicks on the element with the id `update_header`.

### 6. Star Wars Character

**File:** `6-script.js`

Script that fetches the name of a character from the Star Wars API
(`https://swapi-api.hbtn.io/api/people/5/?format=json`)
and displays it in the element with the id `character` using the Fetch API.

### 7. Star Wars Movies

**File:** `7-script.js`

Script that fetches and lists all Star Wars movie titles from the API
(`https://swapi-api.hbtn.io/api/films/?format=json`)
inside a `ul` element with the id `list_movies`.

### 8. Say Hello!

**File:** `8-script.js`

Script that fetches the French translation of the word **"hello"** from the API
(`https://hellosalut.stefanbohacek.com/?lang=fr`)
and displays it in the element with the id `hello`.

The script must work when imported from the `<head>` tag.

## Usage

To test each script:

1. Open the corresponding HTML file in Google Chrome
2. Observe the expected behavior according to the task
3. Use the browser developer console (`F12`) for debugging if necessary

### Example

```bash
# Open the HTML file in Chrome
google-chrome 0-main.html
```

## Technologies Used

* **JavaScript ES6+** – Main programming language
* **DOM API** – Interface for manipulating HTML elements
* **Fetch API** – For making asynchronous HTTP requests
* **Event Listeners** – For handling user interactions

## Author

[SuleimanHajizadeh](https://github.com/SuleimanHajizadeh)

## License

This project is intended for educational purposes as part of the **Holberton School** program.

---

If you want, I can also:

* Convert this into a **proper `README.md`**
* Align it exactly with **Holberton checker expectations**
* Add **code examples** for each task

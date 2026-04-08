# Selenium Automation for prashannachand.com.np

## Overview
This Python script automates end-to-end testing of my personal portfolio website [prashannachand.com.np](https://prashannachand.com.np) using **Selenium WebDriver**. It covers **navigation, project viewing, contact form submission, social media links, and scrolling through sections**, showcasing practical skills in **functional and UI testing**.

## Features

- **Navigation Testing:** Automates clicks on Home, About, Skills, Projects, Contact, and Experiences sections.
- **Projects Section:** Opens each project detail and verifies accessibility.
- **Contact Form Automation:** Fills and submits the "Get in Touch" form with test data.
- **Social Media Links:** Clicks GitHub, LinkedIn, Facebook, and Instagram icons to verify they are functional.
- **Experience Section:** Scrolls through content to ensure visibility and accessibility.
- **Scrolling & Visibility:** Uses `scrollIntoView()` for elements that are dynamically positioned or off-screen.

## Technologies Used

- Python 3.x  
- Selenium WebDriver  
- Brave Browser with Chrome WebDriver  
- JavaScript scroll commands (`execute_script`)  

## Purpose

This automation demonstrates:

- Functional testing of navigation and interactive elements  
- Form and external link validation  
- Handling dynamic elements, overlays, and scrolling  
- End-to-end testing skills applicable to real-world websites  

## How to Run

1. Install Selenium:
```bash
pip install selenium
```
2. Update the Brave browser binary path if necessary:
```python
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
```
3. Run the script:
```bash
python seleniumtest.py
```
4. Observe automated navigation, project interactions, form submissions, and social media link checks.


import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox


def search_google(query, output_text):
    output_text.delete(1.0, tk.END)  # Clear previous results
    # Initialize Chrome driver
    service = Service(executable_path="./chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to url
        driver.get("https://www.google.com")

        # Search for the query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query + Keys.ENTER)

        # Wait for search results to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "rc")))

        search_results = driver.find_elements(By.CLASS_NAME, "rc")

        # Filter relevant links
        relevant_links = [result.find_element(By.TAG_NAME, "a").get_attribute(
            "href") for result in search_results if "example.com" in result.find_element(By.TAG_NAME, "a").get_attribute("href")]

        if relevant_links:
            output_text.insert(tk.END, "Relevant Links:\n")
            for link in relevant_links:
                output_text.insert(tk.END, f"{link}\n")
        else:
            output_text.insert(tk.END, "No relevant links found.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    finally:
        driver.quit()

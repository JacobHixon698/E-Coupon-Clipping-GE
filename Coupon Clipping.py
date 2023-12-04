#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:45:08 2023

Coupon Clipping

@author: jacobhixon
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
import time

# Set up WebDriver
service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the website
    driver.get("https://www.gianteagle.com/coupons")

    # Check and click the cookie consent button
    try:
        accept_cookies_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cm-button"))
        )
        accept_cookies_button.click()
    except Exception as e:
        print("Cookie consent button not found or not clickable:", e)

    # Allow some time for the page to update after handling the popup
    time.sleep(5)

    # Click the dropdown to reveal the Sign In option
    dropdown_selector = "#root > div.Navigation > div > div:nth-child(1) > div.sc-ecbIiB.gSInaM > nav > div:nth-child(7) > button > div > div"
    dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, dropdown_selector))
    )
    dropdown_button.click()

    # Now click the actual Sign In button
    sign_in_button_selector = "#root > div.Navigation > div > div:nth-child(1) > div.sc-ecbIiB.gSInaM > nav > div:nth-child(7) > div > ul > li:nth-child(1) > button > div"
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, sign_in_button_selector))
    )
    sign_in_button.click()

    # Prompt user for credentials
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Wait for the username input field and enter the username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "signInName"))
    )
    username_input.send_keys(username)

    # Find the password input field and enter the password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    # Find and click the submit button
    submit_button = driver.find_element(By.ID, "next")
    submit_button.click()

    # Wait for login to complete
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test-id='HeaderPerksLink']"))
    )

    # Scroll down the page in increments to load all coupons
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(4)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Find all the coupon clip buttons
    try:
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[@aria-label='Clip Coupon']"))
        )
    except Exception as e:
        print("Error finding coupon buttons:", e)
        buttons = []

    # Click each button
    for button in buttons:
        try:
            button.click()
            time.sleep(1)  # Sleep for a bit between clicks to mimic human behavior
        except Exception as e:
            print("Error clicking a button:", e)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()

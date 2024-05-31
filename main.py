import PyPDF2
import itertools
import string
import time
from PyPDF2.errors import PdfReadError

def attempt_password(pdf_file_path, password):
    start_time = time.time()
    print(f"--Cracking start-- Trying password: {password}")
    try:
        with open(pdf_file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            if reader.is_encrypted:
                try:
                    reader.decrypt(password)
                    # Accessing the first page to verify if the password is correct
                    reader.pages[0]
                    end_time = time.time()
                    duration = end_time - start_time
                    print(f"--Cracking success-- Password found: {password} in {duration:.6f} seconds")
                    return True
                except PdfReadError:
                    end_time = time.time()
                    duration = end_time - start_time
                    print(f"--Cracking attempt unsuccessful-- Incorrect password: {password} in {duration:.4f} seconds")
                    return False
    except Exception as e:
        end_time = time.time()
        duration = end_time - start_time
        print(f"--Cracking attempt unsuccessful-- Exception for password: {password} in {duration:.4f} seconds. Error: {e}")
        return False
    end_time = time.time()
    duration = end_time - start_time
    print(f"--Cracking attempt unsuccessful-- Tried password: {password} in {duration:.4f} seconds")
    return False

def brute_force_pdf(pdf_file_path, min_length, max_length):
    start_total_time = time.time()
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(min_length, max_length + 1):
        for password_tuple in itertools.product(characters, repeat=length):
            password = ''.join(password_tuple)
            if attempt_password(pdf_file_path, password):
                end_total_time = time.time()
                total_duration = end_total_time - start_total_time
                print(f"Total cracking time: {total_duration:.6f} seconds")
                return
    end_total_time = time.time()
    total_duration = end_total_time - start_total_time
    print("Password not found")
    print(f"Total cracking time: {total_duration:.6f} seconds")


# Example usage
pdf_file_path = './EMAT-M0044 Introduction to Artificial Intelligence 2024_summer.pdf'
min_length = 3
max_length = 6

brute_force_pdf(pdf_file_path, min_length, max_length)
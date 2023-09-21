- Wiki Search Application

This is a Python application that allows you to search for information on Wikipedia using a simple graphical user interface (GUI). You can enter a word or phrase, and the application will provide you with a summary of the search results from Wikipedia. Additionally, it can read the search results aloud using text-to-speech functionality.

-- Prerequisites

Before running this application, make sure you have the following dependencies installed:

1. Python
2. `tkinter` library for GUI (usually included with Python)
3. `PIL` (Pillow) library for image handling. You can install it using pip:

   pip install Pillow

4. `wikipedia` library for fetching Wikipedia search results. You can install it using pip:

   pip install wikipedia-api

5. `pyttsx3` library for text-to-speech functionality. You can install it using pip:

   pip install pyttsx3

-- How to Use

1. Clone or download the repository containing this code.

2. Run the following command to start the Wiki Search application:

   python wiki_search.py

3. The Wiki Search window will open, displaying the following components:

   - A label with a welcome message and search instructions.
   - An entry field to enter the word or phrase you want to search.
   - A search button represented by an image.
   
4. Enter the word or phrase you want to search in the entry field and click the search button.

5. The application will retrieve the search results from Wikipedia and display the summary in the GUI.

6. You can listen to the search results by clicking the "Play" button.

-- Features

- Searches Wikipedia for the provided word or phrase.
- Displays a summary of the search results.
- Provides text-to-speech functionality to read the search results aloud.

-- Contributing

If you'd like to contribute to this project or add more features to the Wiki Search application, feel free to make your own modifications and enhancements.

-- License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

**Note**: This README assumes that you have the necessary dependencies installed and correctly configured. If you encounter any issues or errors, please ensure that your Python environment is set up correctly.
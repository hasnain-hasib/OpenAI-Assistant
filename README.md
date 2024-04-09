

# OpenAI Assistant

A simple web application that uses the OpenAI API to provide a conversational assistant.

## Features

- Allows users to input a prompt or question
- Sends the prompt to the OpenAI API and displays the generated response
- Provides a clean and responsive user interface built with Bootstrap

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/openai-assistant.git
   ```

2. Change to the project directory:
   ```
   cd openai-assistant
   ```

3. Install the required dependencies:
   ```
   pip install fastapi openai uvicorn
   ```

4. Set your OpenAI API key:
   ```python
   openai.api_key = "YOUR_OPENAI_API_KEY"
   ```

5. Start the server:
   ```
   python main.py
   ```

6. Open your web browser and visit `http://localhost:8000` to use the application.

## Usage

1. Enter a prompt or question in the text area.
2. Click the "Submit" button.
3. The application will send the prompt to the OpenAI API and display the generated response.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python.
- [OpenAI API](https://openai.com/api/) - A powerful language model that can be used for a variety of tasks, including conversational assistants.
- [Bootstrap](https://getbootstrap.com/) - A popular CSS framework for building responsive and mobile-first websites.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

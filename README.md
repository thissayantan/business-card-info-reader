# Business Card Information Reader

This Python application leverages advanced machine learning models from OpenAI and Google (Gemini) to analyze images of business cards and extract valuable information such as names, job titles, company details, and contact information.

## Features

- **Image Analysis**: Analyze business card images to extract detailed contact information.
- **Multiple Models Support**: Supports both OpenAI and Google Gemini models for image analysis.
- **Flexible Input**: Accepts images via URLs and allows the selection of the analysis model through command-line arguments.

## Installation

This project uses Poetry for dependency management. To set up the project:

1. Clone the repository:
   ```bash
   git clone git@github.com:thissayantan/business-card-info-reader.git
   ```
2. Navigate to the project directory:
   ```bash
   cd business-card-info-reader
   ```
3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

Run the application using the following command:

```bash
poetry run python main.py --image_url [IMAGE_URL] --model_name [MODEL_NAME]
```

- `IMAGE_URL` (optional): URL of the business card image to analyze. If not provided, a default image is used.
- `MODEL_NAME` (optional): Specify `google` to use the Google Gemini model. By default, the OpenAI model is used.

Example:
```bash
poetry run python main.py --image_url "http://example.com/image.jpg" --model_name "google"
```

## Configuration

Ensure you have the following environment variables set:

- `OPENAI_API_KEY`: API key for OpenAI.
- `GOOGLE_API_KEY`: API key for Google Gemini.

These are necessary for the respective models to function correctly.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under MIT License. For more information, please see the [LICENSE](https://github.com/thissayantan/business-card-info-reader/blob/main/LICENSE) file.

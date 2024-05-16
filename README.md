# Cyber CP Demo Application

Welcome to the Cyber CP Demo, a fun and interactive web application that uses Gradio-Lite to calculate compatibility points and generate story prompts based on the names of two individuals. This application is entirely browser-based and does not require any server-side infrastructure.

## Features

- **Character Trait Analysis**: The application calculates and displays character traits for each individual based on a SHA256 hash of their name.
- **Compatibility Points Calculation**: It computes a 'cp value' between two individuals using a custom algorithm that includes a Hamming distance calculation and character differences.
- **Story Prompt Generation**: Generates a story prompt that suggests a type of relationship story based on the calculated traits and cp value.

## How to Use

1. Enter the name of the first individual into the "A的名字" (Name A) textbox.
2. Enter the name of the second individual into the "B的名字" (Name B) textbox.
3. Click the "计算cp值" (Calculate cp value) button to compute the compatibility points.
4. Once the cp value is calculated, click the "生成故事Prompt" (Generate story Prompt) button to produce a story prompt.
5. The generated story prompt and cp value will be displayed, which you can then use to create a story.

### Note

- The application uses a hash of the names provided for its calculations, which may not correspond to real personality traits.
- The story types and traits are randomly selected based on the hash and are for entertainment purposes only.

## Compatibility

This application is designed to work on modern web browsers that support JavaScript and WebAssembly.

## Credits

- Gradio-Lite: For providing the browser-based interface for this application.
- SHA256 Hashing: For generating a unique hash based on the input names.

## License

This application is open-source and available under the [MIT License](LICENSE).

## Disclaimer

The application is for entertainment purposes only and does not provide psychological or personality assessments.

## Support

For any questions or support, please reach out through the provided contact methods.

## Links

- [Gradio Website](https://www.gradio.app/)
- [Moonshot AI](https://kimi.moonshot.cn/chat/)

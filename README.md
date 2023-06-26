<a href="https://www.buymeacoffee.com/metimol" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

### Hello everyone!

Specify what you want it to build, the AI asks for clarification, and then builds it.

#### Free-GPT-Engineer is made to be easy to adapt, extend, and make your agent learn how you want your code to look. It generates an entire codebase based on a prompt.
It **absolutely FREE.** You don't need to using Openai API Key.

This project based on the [GPT-Engineer repository](https://github.com/AntonOsika/gpt-engineer), version **0.0.7**

## Project philosophy
- Simple to get value
- Flexible and easy to add new own "AI steps". See `steps.py`.
- Incrementally build towards a user experience of:
  1. high level prompting
  2. giving feedback to the AI that it will remember over time
- Fast handovers back and forth between AI and human
- Simplicity, all computation is "resumable" and persisted to the filesystem

## Usage

For installing **Free-GPT-Engineer** run this commands:
- `git clone https://github.com/Metim0l/free-gpt-engineer.git`
- `cd free-gpt-engineer`
- `pip install -r requirements.txt`

**Run**:
- Create an empty folder inside the repo, in **projects** folder.
- Fill in the `prompt` file in your new folder
- Run command `python main.py projects/new_folder`

**Results**
- Check the generated files in `projects/my-new-project/workspace`

## Example

https://github.com/AntonOsika/gpt-engineer/assets/4467025/6e362e45-4a94-4b0d-973d-393a31d92d9b

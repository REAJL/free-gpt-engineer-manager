I have recently designed a script based on the integration of GPT-Engineer, made available by https://github.com/Metim0l/free-gpt-engineer. I have decided to share this script with you. It is a graphical manager specifically developed to optimize the user experience of the Free-GPT-Engineer program. This file is the result of numerous hours of work, aiming to create an intuitive and user-friendly interface for seamless manipulation and control of the program's functionalities. I hope that this tool proves valuable to you in your own projects

Coffee for Metim0l! He's thirsty <3

<a href="https://www.buymeacoffee.com/metimol"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee :)&emoji=&slug=metimol&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff" /></a>

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
- `git clone https://github.com/arkadawa/free-gpt-engineer-manager.git`
- `cd free-gpt-engineer-manager`
- `pip install -r requirements.txt`


** RUN WITH MANAGER  ** (Tested on Ubuntu 22.04.2 LTS)
- Run command `python3 freegptmanager.py`
- Press Delete Files
- Press Create
- Edit Prompt
- And start script
- Export and renew 


** RUN WITHOUT MANAGER **:
- Create an empty folder inside the repo, in **projects** folder.
- Fill in the `prompt` file in your new folder
- Run command `python main.py projects/new_folder`

**Results**
- Check the generated files in `projects/my-new-project/workspace`


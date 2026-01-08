# My-First-DC-Bot
I built this DC Bot some time ago(2022) as a way to get into python because at the time when our discord was very active there were already several music/management bots added by other people but they kept breaking so i just made my own so i would be able to manage it better and centralize the functions rather than have many bots

Discord Bot Project
​A feature-rich Discord bot built using Python and the discord.py library. This bot includes automated moderation, role management, and personalized member greetings.  

​🚀 Features
​Member Greetings: Automatically sends a Direct Message (DM) to new members when they join the server.  
​Word Filtering: Monitors messages for the word "sleep" and automatically deletes them to maintain chat standards.  
​Role Management: * !assign: Grants the user the Honchoss role.  
​!remove: Revokes the Honchoss role from the user.  
​Permission-Based Commands: Includes a !secret command accessible only to users with the Honchoss role.  
​Automated Logging: Saves bot events and errors to a local Discord.log file for debugging. 

​🛠️ Installation & Setup
​1. Prerequisites
​Ensure you have Python 3.8+ installed. You will also need to create a bot application in the Discord Developer Portal and enable Server Members Intent and Message Content Intent.
​2. Clone the Repository
git clone <your-repository-url>
cd <project-folder>
3. Install Dependencies
​Install the required libraries using pip:
pip install discord.py python-dotenv
4. Environment Configuration
​Create a .env file in the root directory and add your bot token:
DISCORD_TOKEN=your_token_here

🎮 Usage
​To start the bot, run the following command in your terminal
python <whatever you named it>.py

📂 File Structure
<whatever you named it>.py: The main bot logic.  
​.env: Stores sensitive credentials (ignored by git).
​Discord.log: Generated log file for monitoring bot activity.  

If anything wasnt clear ive listed some resources for you to refer to.

​Sources & References
​Project Code Analysis: Derived directly from the provided .py script, identifying specific imports like discord.ext.commands and dotenv.  
​Library Documentation: Based on discord.py standards for event listeners (on_ready, on_member_join) and command decorators.  
​Discord Developer Portal: Requirements for intents.message_content and intents.members established in the code.

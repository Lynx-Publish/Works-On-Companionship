import discord
from discord.ext import commands

#Crafted by alerthi_there discord or Lynx-publish on github.


# Intents for the bot
intents = discord.Intents.default()

import os

# Bot instance
bot = commands.Bot(command_prefix="/", intents=intents)

# Dictionary to store user preferences
user_preferences = {}


# Custom Select class for dropdown menus
class CustomSelect(discord.ui.Select):
    def __init__(self, placeholder, options):
        super().__init__(placeholder=placeholder, options=options, max_values=len(options))
        self.placeholder = placeholder

    async def callback(self, interaction: discord.Interaction):
        username = interaction.user.name
        preferences_selected = interaction.data["values"]
        # Update user preferences dictionary
        if username not in user_preferences:
            user_preferences[username] = {}
        user_preferences[username][self.placeholder] = preferences_selected
        # Send confirmation message
        await interaction.response.edit_message(content=f"{self.placeholder}: {', '.join(preferences_selected)}")


# Custom View class for organizing dropdowns
class CustomView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.index = 0

    def add_item(self, item):
        if self.index == 25:
            self.stop()
            raise ValueError('could not find open space for item')
        super().add_item(item)
        self.index += 1


# Command to start the menu
@bot.command()
async def register(ctx):
    embed = discord.Embed(title="Welcome to the dating preference setup!", color=0xff69b4)
    await ctx.send(embed=embed)

    # Creating views
    user_info_view1 = CustomView()
    user_info_view2 = CustomView()
    user_info_view3 = CustomView()
    user_info_view4 = CustomView()
    mate_info_view1 = CustomView()
    mate_info_view2 = CustomView()
    mate_info_view3 = CustomView()
    mate_info_view4 = CustomView()

    # User's info
    user_info_options1 = [
        discord.SelectOption(label="Male", value="Male"),
        discord.SelectOption(label="Female", value="Female"),
        discord.SelectOption(label="Non-binary", value="Non-binary"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view1.add_item(CustomSelect("Gender", user_info_options1))

    user_info_options2 = [
        discord.SelectOption(label="Heterosexual", value="Heterosexual"),
        discord.SelectOption(label="Homosexual", value="Homosexual"),
        discord.SelectOption(label="Bisexual", value="Bisexual"),
        discord.SelectOption(label="Pansexual", value="Pansexual"),
        discord.SelectOption(label="Asexual", value="Asexual"),
        discord.SelectOption(label="Other", value="Other")
    ]
    user_info_view1.add_item(CustomSelect("Sexuality", user_info_options2))

    user_info_options3 = [
        discord.SelectOption(label="13", value="13"),
        discord.SelectOption(label="14", value="14"),
        discord.SelectOption(label="15", value="15"),
        discord.SelectOption(label="16", value="16"),
        discord.SelectOption(label="17", value="17"),
        discord.SelectOption(label="N/A", value="N/A")
    ]
    user_info_view1.add_item(CustomSelect("Age", user_info_options3))

    user_info_options4 = [
        discord.SelectOption(label="GMT-12:00", value="GMT-12:00"),
        discord.SelectOption(label="GMT-11:00", value="GMT-11:00"),
        discord.SelectOption(label="GMT-10:00", value="GMT-10:00"),
        # Add more time zone options as needed
        discord.SelectOption(label="GMT+13:00", value="GMT+13:00"),
        discord.SelectOption(label="GMT+14:00", value="GMT+14:00"),
    ]
    user_info_view1.add_item(CustomSelect("Time Zone", user_info_options4))

    user_info_options5 = [
        discord.SelectOption(label="Introvert", value="Introvert"),
        discord.SelectOption(label="Extrovert", value="Extrovert"),
        discord.SelectOption(label="Ambivert", value="Ambivert"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view2.add_item(CustomSelect("Personality Type", user_info_options5))

    user_info_options6 = [
        discord.SelectOption(label="Art", value="Art"),
        discord.SelectOption(label="Sports", value="Sports"),
        discord.SelectOption(label="Music", value="Music"),
        discord.SelectOption(label="Reading", value="Reading"),
        discord.SelectOption(label="Gaming", value="Gaming"),
        discord.SelectOption(label="Cooking", value="Cooking"),
        discord.SelectOption(label="Other", value="Other")
    ]
    user_info_view2.add_item(CustomSelect("Hobbies", user_info_options6))

    user_info_options7 = [
        discord.SelectOption(label="Slim", value="Slim"),
        discord.SelectOption(label="Average", value="Average"),
        discord.SelectOption(label="Athletic", value="Athletic"),
        discord.SelectOption(label="Curvy", value="Curvy"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view3.add_item(CustomSelect("Body Type", user_info_options7))

    user_info_options8 = [
        discord.SelectOption(label="Caucasian", value="Caucasian"),
        discord.SelectOption(label="Black", value="Black"),
        discord.SelectOption(label="Asian", value="Asian"),
        discord.SelectOption(label="Hispanic", value="Hispanic"),
        discord.SelectOption(label="Other", value="Other"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view3.add_item(CustomSelect("Race", user_info_options8))

    user_info_options9 = [
        discord.SelectOption(label="Slow", value="Slow"),
        discord.SelectOption(label="Normal", value="Normal"),
        discord.SelectOption(label="Fast", value="Fast"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view4.add_item(CustomSelect("Relationship Speed", user_info_options9))

    user_info_options10 = [
        discord.SelectOption(label="Yes", value="Yes"),
        discord.SelectOption(label="No", value="No"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view4.add_item(CustomSelect("NSFW Content", user_info_options10))

    user_info_options11 = [
        discord.SelectOption(label="Engineering", value="Engineering"),
        discord.SelectOption(label="Medical/Healthcare", value="Medical/Healthcare"),
        discord.SelectOption(label="Information Technology", value="Information Technology"),
        discord.SelectOption(label="Business/Finance", value="Business/Finance"),
        discord.SelectOption(label="Art/Design", value="Art/Design"),
        discord.SelectOption(label="Education", value="Education"),
        discord.SelectOption(label="Other", value="Other"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view4.add_item(CustomSelect("Career Interests", user_info_options11))

    user_info_options12 = [
        discord.SelectOption(label="Within an hour", value="Within an hour"),
        discord.SelectOption(label="Within a day", value="Within a day"),
        discord.SelectOption(label="Within a few days", value="Within a few days"),
        discord.SelectOption(label="Varies", value="Varies"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    user_info_view4.add_item(CustomSelect("Typical Response Time", user_info_options12))

    # Mate's preferences
    mate_info_options1 = [
        discord.SelectOption(label="Male", value="Male"),
        discord.SelectOption(label="Female", value="Female"),
        discord.SelectOption(label="Non-binary", value="Non-binary"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view1.add_item(CustomSelect("Desired Gender", mate_info_options1))

    mate_info_options2 = [
        discord.SelectOption(label="Heterosexual", value="Heterosexual"),
        discord.SelectOption(label="Homosexual", value="Homosexual"),
        discord.SelectOption(label="Bisexual", value="Bisexual"),
        discord.SelectOption(label="Pansexual", value="Pansexual"),
        discord.SelectOption(label="Asexual", value="Asexual"),
        discord.SelectOption(label="Other", value="Other")
    ]
    mate_info_view1.add_item(CustomSelect("Desired Sexuality", mate_info_options2))

    mate_info_options3 = [
        discord.SelectOption(label="13", value="13"),
        discord.SelectOption(label="14", value="14"),
        discord.SelectOption(label="15", value="15"),
        discord.SelectOption(label="16", value="16"),
        discord.SelectOption(label="17", value="17"),
        discord.SelectOption(label="N/A", value="N/A")
    ]
    mate_info_view1.add_item(CustomSelect("Desired Age", mate_info_options3))

    mate_info_options4 = [
        discord.SelectOption(label="GMT-12:00", value="GMT-12:00"),
        discord.SelectOption(label="GMT-11:00", value="GMT-11:00"),
        discord.SelectOption(label="GMT-10:00", value="GMT-10:00"),
        # Add more time zone options as needed
        discord.SelectOption(label="GMT+13:00", value="GMT+13:00"),
        discord.SelectOption(label="GMT+14:00", value="GMT+14:00"),
    ]
    mate_info_view1.add_item(CustomSelect("Desired Time Zone", mate_info_options4))

    mate_info_options5 = [
        discord.SelectOption(label="Introvert", value="Introvert"),
        discord.SelectOption(label="Extrovert", value="Extrovert"),
        discord.SelectOption(label="Ambivert", value="Ambivert"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view2.add_item(CustomSelect("Desired Personality Type", mate_info_options5))

    mate_info_options6 = [
        discord.SelectOption(label="Art", value="Art"),
        discord.SelectOption(label="Sports", value="Sports"),
        discord.SelectOption(label="Music", value="Music"),
        discord.SelectOption(label="Reading", value="Reading"),
        discord.SelectOption(label="Gaming", value="Gaming"),
        discord.SelectOption(label="Cooking", value="Cooking"),
        discord.SelectOption(label="Other", value="Other")
    ]
    mate_info_view2.add_item(CustomSelect("Desired Hobbies", mate_info_options6))

    mate_info_options7 = [
        discord.SelectOption(label="Slim", value="Slim"),
        discord.SelectOption(label="Average", value="Average"),
        discord.SelectOption(label="Athletic", value="Athletic"),
        discord.SelectOption(label="Curvy", value="Curvy"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view3.add_item(CustomSelect("Desired Body Type", mate_info_options7))

    mate_info_options8 = [
        discord.SelectOption(label="Caucasian", value="Caucasian"),
        discord.SelectOption(label="Black", value="Black"),
        discord.SelectOption(label="Asian", value="Asian"),
        discord.SelectOption(label="Hispanic", value="Hispanic"),
        discord.SelectOption(label="Other", value="Other"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view3.add_item(CustomSelect("Desired Race", mate_info_options8))

    mate_info_options9 = [
        discord.SelectOption(label="Slow", value="Slow"),
        discord.SelectOption(label="Normal", value="Normal"),
        discord.SelectOption(label="Fast", value="Fast"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view4.add_item(CustomSelect("Desired Relationship Speed", mate_info_options9))

    mate_info_options10 = [
        discord.SelectOption(label="Yes", value="Yes"),
        discord.SelectOption(label="No", value="No"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view4.add_item(CustomSelect("Desired NSFW Content", mate_info_options10))

    mate_info_options11 = [
        discord.SelectOption(label="Engineering", value="Engineering"),
        discord.SelectOption(label="Medical/Healthcare", value="Medical/Healthcare"),
        discord.SelectOption(label="Information Technology", value="Information Technology"),
        discord.SelectOption(label="Business/Finance", value="Business/Finance"),
        discord.SelectOption(label="Art/Design", value="Art/Design"),
        discord.SelectOption(label="Education", value="Education"),
        discord.SelectOption(label="Other", value="Other"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view4.add_item(CustomSelect("Desired Career Interests", mate_info_options11))

    mate_info_options12 = [
        discord.SelectOption(label="Within an hour", value="Within an hour"),
        discord.SelectOption(label="Within a day", value="Within a day"),
        discord.SelectOption(label="Within a few days", value="Within a few days"),
        discord.SelectOption(label="Varies", value="Varies"),
        discord.SelectOption(label="Prefer not to say", value="Prefer not to say")
    ]
    mate_info_view4.add_item(CustomSelect("Desired Typical Response Time", mate_info_options12))

    # Send the views
    embed = discord.Embed(title="Welcome to Singularity!", color=0xff69b4)
    await ctx.send(embed=embed)

    embed = discord.Embed(title="Your info", color=0xff69b4)
    await ctx.send(embed=embed)

    await ctx.send(view=user_info_view1)
    await ctx.send(view=user_info_view2)
    await ctx.send(view=user_info_view3)
    await ctx.send(view=user_info_view4)
    embed = discord.Embed(title="Your perfect matches info", color=0xff69b4)
    await ctx.send(embed=embed)
    await ctx.send(view=mate_info_view1)
    await ctx.send(view=mate_info_view2)
    await ctx.send(view=mate_info_view3)
    await ctx.send(view=mate_info_view4)
    embed = discord.Embed(title="Created by alterhi_there", color=0x597b99)
    await ctx.send(embed=embed)


# Command to save user preferences to a .txt file
@bot.command()
async def save(ctx):
    username = ctx.author.name
    user_prefs = user_preferences.get(username)
    print(username)
    print(user_prefs)
    if not user_prefs:
        await ctx.send("User preferences not found. Please fill out the preferences using the /start command first.")
        return

    # Save preferences to a .txt file
    with open(f"{username}_preferences.txt", "w") as file:
        for category, preferences in user_prefs.items():
            file.write(f"{category}:\n")
            for preference in preferences:
                file.write(f"  - {preference}\n")

    await ctx.send(f"User preferences saved as {username}_preferences.txt")

##---------------------------------------------------------------

@bot.command()
async def matchme(ctx):
    username = ctx.author.name
    user_prefs = load_user_prefs(username)
    if not user_prefs:
        await ctx.send("Please create an account by using the /register command first.")
        return

    # Find potential matches
    matches = []  # Store matches here
    for file_name in os.listdir():
        if file_name.endswith("_preferences.txt"):
            mate_name = file_name[:-16]  # Extract mate's username from file name
            if mate_name == username:
                continue

            mate_prefs = load_user_prefs(mate_name)
            if mate_prefs:
                compatibility_score = calculate_compatibility(user_prefs, mate_prefs)

                # Add mate and score to matches
                matches.append((mate_name, compatibility_score))

    # Sort matches by compatibility score
    matches.sort(key=lambda x: x[1], reverse=True)

    # Select the top 10 matches that have a score greater than 0
    top_matches = [(mate, score) for mate, score in matches if score > 0][:10]

    if top_matches:
        # Send the top matches
        response = "Top 10 matches and their percentages:\n"
        for mate, score in top_matches:
            response += f"{mate}: {score}%\n"
        await ctx.send(response)
    else:
        await ctx.send("No matches found.")



# Function to load user preferences from file
def load_user_prefs(username):
    user_filename = f"{username}_preferences.txt"
    if os.path.exists(user_filename):
        user_prefs = {}
        with open(user_filename, "r") as file:
            lines = file.readlines()
            category = None
            for line in lines:
                if ":" in line:
                    category = line.split(":")[0].strip()
                    user_prefs[category] = []
                elif category:
                    preference = line.strip().replace("-", "").replace("•", "")
                    if preference:
                        user_prefs[category].append(preference)
        return user_prefs
    else:
        return None


# Function to calculate compatibility score between two users
def calculate_compatibility(user_prefs, mate_prefs):
    compatibility_score = 0
    total_preferences = 0

    # Get user's sexuality, gender, NSFW, and age preferences
    user_sexuality = user_prefs.get("Sexuality", ["Other"])[0]
    user_gender = user_prefs.get("Gender", ["Other"])[0]
    user_nsfw = user_prefs.get("NSFW Content", ["Other"])[0]
    user_age = user_prefs.get("Age", ["Other"])[0]

    # Get mate's sexuality, gender, NSFW, and age preferences
    mate_sexuality = mate_prefs.get("Sexuality", ["Other"])[0]
    mate_gender = mate_prefs.get("Gender", ["Other"])[0]
    mate_nsfw = mate_prefs.get("NSFW Content", ["Other"])[0]
    mate_age = mate_prefs.get("Age", ["Other"])[0]

    # Check sexual compatibility
    if user_sexuality == "Heterosexual":
        if mate_sexuality not in ["Female", "Non-binary"]:
            return 0
    elif user_sexuality == "Homosexual":
        if mate_sexuality != user_gender:
            return 0
    elif user_sexuality == "Bisexual":
        if mate_sexuality == "Asexual":
            return 0
    elif user_sexuality == "Asexual":
        if mate_sexuality != "Asexual":
            return 0

    # Check gender compatibility
    if user_gender == mate_gender:
        # If both genders are the same, make sure mate is interested in the same gender
        if mate_gender == "Non-binary":
            if user_sexuality != "Bisexual":
                return 0
        elif mate_gender != user_sexuality:
            return 0
    else:
        # If both genders are different, make sure mate is interested in the user's gender
        if user_gender == "Male":
            if mate_gender not in ["Male", "Non-binary"]:
                return 0
            elif user_sexuality == "Heterosexual" and mate_sexuality != "Female":
                return 0
        elif user_gender == "Female":
            if mate_gender not in ["Female", "Non-binary"]:
                return 0
            elif user_sexuality == "Heterosexual" and mate_sexuality != "Male":
                return 0
        elif user_gender == "Non-binary":
            if mate_gender != "Non-binary":
                return 0
            elif user_sexuality == "Heterosexual" and mate_sexuality not in ["Male", "Female"]:
                return 0

    # Check NSFW content compatibility
    if user_nsfw != mate_nsfw:
        return 0

    # Check age compatibility
    if user_age != mate_age:
        return 0

    # Compare preferences
    for category, user_preferences in user_prefs.items():
        if category in mate_prefs:
            mate_preferences = mate_prefs[category]
            for preference in user_preferences:
                total_preferences += 1
                if preference in mate_preferences:
                    compatibility_score += 1

    if total_preferences == 0:
        return 0
    else:
        return (compatibility_score / total_preferences) * 100






##--------------------------------------------------------
@bot.command()
async def helpme(ctx):
    help_message = (
        "**Welcome to Singularity Bot Help!**\n\n"
        "**1. Register Preferences:**\n"
        "Use `/register` command to set up your dating preferences.\n\n"
        "**2. Save Preferences:**\n"
        "Use `/save` command to save your preferences to a file.\n\n"
        "**3. Find a Match:**\n"
        "Use `/matchme` command to find a match based on your preferences.\n\n"
        "**Command Usage:**\n"
        "`/register` - Start the preference setup process.\n"
        "`/save` - Save your preferences to a file.\n"
        "`/matchme` - Find a match based on your preferences.\n"
        "`/help` - Display this help message.\n"
        "`/listusers` - Displays a list of all users.\n"
        "`/forget` - Remove all of your data.\n\n"
        "`/userview` - Give the users discord tag and see their data.\n\n"
        "**Note:**\n"
        "Please ensure you have set up your preferences before using the match command.\n"
        "For further assistance, contact the developer alerthi_there."
    )
    embed = discord.Embed(title="Singularity Bot Help", description=help_message, color=0x00ff00)
    await ctx.send(embed=embed)


# Command to forget user data
@bot.command()
async def forget(ctx):
    username = ctx.author.name
    filename = f"{username}_preferences.txt"
    try:
        os.remove(filename)
        await ctx.send(f"All data for {username} has been forgotten.")
    except FileNotFoundError:
        await ctx.send(f"No data found for {username}.")

@bot.command()
async def listusers(ctx):
    file_list = [filename[:-16] for filename in os.listdir() if filename.endswith("_preferences.txt")]
    if file_list:
        users = "\n".join(file_list)
        await ctx.send(f"Registered users:\n{users}")
    else:
        await ctx.send("No registered users found.")

@bot.command()
async def userview(ctx, username: str):
    user_prefs = load_user_prefs(username)
    if not user_prefs:
        await ctx.send(f"No preferences found for {username}.")
        return

    # Format user preferences for display
    preferences_text = ""
    for category, preferences in user_prefs.items():
        preferences_text += f"{category}:\n"
        for preference in preferences:
            preferences_text += f"  - {preference}\n"

    await ctx.send(f"**Preferences for {username}:**\n```{preferences_text}```")



bot.run("YOUR TOKEN HERE")

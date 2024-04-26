import discord
from discord.ext import commands

#Crafted by alerthi_there discord or Lynx-publish on github.


# Intents for the bot
intents = discord.Intents.default()

import os

# Bot instance
bot = commands.Bot(command_prefix="..", intents=intents)

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
    await ctx.send("Welcome to the dating preference setup!")

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
        discord.SelectOption(label="13-17", value="13-17"),
        discord.SelectOption(label="18-25", value="18-25"),
        discord.SelectOption(label="26-35", value="26-35"),
        discord.SelectOption(label="36-45", value="36-45"),
        discord.SelectOption(label="46-55", value="46-55"),
        discord.SelectOption(label="56+", value="56+")
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
        discord.SelectOption(label="13-17", value="13-17"),
        discord.SelectOption(label="18-25", value="18-25"),
        discord.SelectOption(label="26-35", value="26-35"),
        discord.SelectOption(label="36-45", value="36-45"),
        discord.SelectOption(label="46-55", value="46-55"),
        discord.SelectOption(label="56+", value="56+")
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
    await ctx.send("**_________!WELCOME TO SINGULARITY!__________**")
    await ctx.send("**_________<Your info>__________**")
    await ctx.send(view=user_info_view1)
    await ctx.send(view=user_info_view2)
    await ctx.send(view=user_info_view3)
    await ctx.send(view=user_info_view4)
    await ctx.send("**_________<Your perfect matches info>__________**")
    await ctx.send(view=mate_info_view1)
    await ctx.send(view=mate_info_view2)
    await ctx.send(view=mate_info_view3)
    await ctx.send(view=mate_info_view4)
    await ctx.send("**_________!---created by alerthi_there----!__________**")


# Command to save user preferences to a .txt file
@bot.command()
async def save(ctx):
    username = ctx.author.name
    user_prefs = user_preferences.get(username)
    print(username)
    print(user_prefs)
    if not user_prefs:
        await ctx.send("User preferences not found. Please fill out the preferences using the .start command first.")
        return

    # Save preferences to a .txt file
    with open(f"{username}_preferences.txt", "w") as file:
        for category, preferences in user_prefs.items():
            file.write(f"{category}:\n")
            for preference in preferences:
                file.write(f"  - {preference}\n")

    await ctx.send(f"User preferences saved as {username}_preferences.txt")


# Command to find a match and calculate compatibility score
# Command for matching users
@bot.command()
async def matchme(ctx):
    username = ctx.author.name
    user_prefs = user_preferences.get(username)
    if not user_prefs:
        await ctx.send("Please create an account by using the .register command first.")
        return

    # Get user's sexuality and gender preferences
    user_sexuality = user_prefs.get("Sexuality", ["Other"])[0]
    user_gender = user_prefs.get("Gender", ["Other"])[0]

    # Find potential matches
    matched_users = []
    for user, preferences in user_preferences.items():
        if user == username:
            continue
        # Check if the user meets the criteria for a match
        mate_sexuality = preferences.get("Sexuality", ["Other"])[0]
        mate_gender = preferences.get("Gender", ["Other"])[0]

        # Check if user's gender preference matches mate's gender
        if user_gender == "Male" and mate_gender not in ["Male", "Non-binary"]:
            continue
        elif user_gender == "Female" and mate_gender not in ["Female", "Non-binary"]:
            continue
        elif user_gender == "Non-binary" and mate_gender == "Male" and mate_sexuality != "Heterosexual":
            continue
        elif user_gender == "Non-binary" and mate_gender == "Female" and mate_sexuality != "Heterosexual":
            continue

        # Check if user's sexuality preference matches mate's sexuality
        if user_sexuality == "Heterosexual" and mate_sexuality not in ["Female", "Non-binary"]:
            continue
        elif user_sexuality == "Homosexual" and mate_sexuality not in ["Male", "Non-binary"]:
            continue
        elif user_sexuality == "Bisexual" and mate_sexuality == "Asexual":
            continue
        elif user_sexuality == "Asexual" and mate_sexuality != "Asexual":
            continue

        matched_users.append((user, preferences))

    if matched_users:
        # Calculate compatibility score
        compatibility_scores = {}
        for matched_user, matched_preferences in matched_users:
            compatibility_score = 0
            # Adjust score based on matching preferences
            for category, preferences in user_prefs.items():
                if category in matched_preferences:
                    for preference in preferences:
                        if preference in matched_preferences[category]:
                            compatibility_score += 1
            compatibility_scores[matched_user] = compatibility_score

        # Sort by compatibility score
        sorted_matches = sorted(compatibility_scores.items(), key=lambda x: x[1], reverse=True)
        best_match_user, best_match_score = sorted_matches[0]

        # Send the best match
        await ctx.send(f"Best match found for {username} with a compatibility score of {best_match_score}: {best_match_user}")
    else:
        await ctx.send("No match found.")

@bot.command()
async def helpme(ctx):
    help_message = (
        "**Welcome to Singularity Bot Help!**\n\n"
        "**1. Register Preferences:**\n"
        "Use `..register` command to set up your dating preferences.\n\n"
        "**2. Save Preferences:**\n"
        "Use `..save` command to save your preferences to a file.\n\n"
        "**3. Find a Match:**\n"
        "Use `..matchme` command to find a match based on your preferences.\n\n"
        "**Command Usage:**\n"
        "`..register` - Start the preference setup process.\n"
        "`..save` - Save your preferences to a file.\n"
        "`..matchme` - Find a match based on your preferences.\n"
        "`..help` - Display this help message.\n\n"
        "**Note:**\n"
        "Please ensure you have set up your preferences before using the match command.\n"
        "For further assistance, contact the developer."
    )
    await ctx.send(help_message)

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


bot.run("MTIzMzI3ODYxNjk5ODExNzQ2OQ.Ge7-gn.u4wKC5sp_JJt2eGIg-8hgjXDcc4gh5_g1sz8xc")

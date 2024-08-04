import discord
from discord.ext import commands

# Define the bot with a command prefix
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# Calculator command
@bot.command(name="calc", help="Performs basic arithmetic operations. Usage: !calc <num1> <operation> <num2>")
async def calculate(ctx, num1: float, operation: str, num2: float):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                await ctx.send("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            await ctx.send("Invalid operation. Please use one of the following: +, -, *, /")
            return

        await ctx.send(f"The result of {num1} {operation} {num2} is {result}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Run the bot with your token
bot.run()
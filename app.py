{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN4GQ1egS2jDUpBlvDbUPo8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/syedaayesha2309/test-scientific-calculator/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "def scientific_calculator():\n",
        "    print(\"Welcome to the Scientific Calculator!\")\n",
        "    print(\"Select the operation you want to perform:\")\n",
        "    print(\"1. Addition (+)\")\n",
        "    print(\"2. Subtraction (-)\")\n",
        "    print(\"3. Multiplication (*)\")\n",
        "    print(\"4. Division (/)\")\n",
        "    print(\"5. Exponential (x^y)\")\n",
        "    print(\"6. Square root (√x)\")\n",
        "    print(\"7. Logarithm (log base 10)\")\n",
        "    print(\"8. Sine (sin)\")\n",
        "    print(\"9. Cosine (cos)\")\n",
        "    print(\"10. Tangent (tan)\")\n",
        "    print(\"11. Factorial (n!)\")\n",
        "    print(\"12. Exit\")\n",
        "\n",
        "    while True:\n",
        "        choice = input(\"\\nEnter the number of the operation you want to perform (1-12): \")\n",
        "\n",
        "        if choice == '1':  # Addition\n",
        "            num1 = float(input(\"Enter first number: \"))\n",
        "            num2 = float(input(\"Enter second number: \"))\n",
        "            print(f\"The result is: {num1 + num2}\")\n",
        "\n",
        "        elif choice == '2':  # Subtraction\n",
        "            num1 = float(input(\"Enter first number: \"))\n",
        "            num2 = float(input(\"Enter second number: \"))\n",
        "            print(f\"The result is: {num1 - num2}\")\n",
        "\n",
        "        elif choice == '3':  # Multiplication\n",
        "            num1 = float(input(\"Enter first number: \"))\n",
        "            num2 = float(input(\"Enter second number: \"))\n",
        "            print(f\"The result is: {num1 * num2}\")\n",
        "\n",
        "        elif choice == '4':  # Division\n",
        "            num1 = float(input(\"Enter first number: \"))\n",
        "            num2 = float(input(\"Enter second number: \"))\n",
        "            if num2 != 0:\n",
        "                print(f\"The result is: {num1 / num2}\")\n",
        "            else:\n",
        "                print(\"Error! Division by zero.\")\n",
        "\n",
        "        elif choice == '5':  # Exponential\n",
        "            base = float(input(\"Enter the base: \"))\n",
        "            exp = float(input(\"Enter the exponent: \"))\n",
        "            print(f\"The result is: {math.pow(base, exp)}\")\n",
        "\n",
        "        elif choice == '6':  # Square root\n",
        "            num = float(input(\"Enter the number: \"))\n",
        "            if num >= 0:\n",
        "                print(f\"The square root of {num} is: {math.sqrt(num)}\")\n",
        "            else:\n",
        "                print(\"Error! Cannot calculate the square root of a negative number.\")\n",
        "\n",
        "        elif choice == '7':  # Logarithm\n",
        "            num = float(input(\"Enter the number: \"))\n",
        "            if num > 0:\n",
        "                print(f\"The logarithm base 10 of {num} is: {math.log10(num)}\")\n",
        "            else:\n",
        "                print(\"Error! Logarithm undefined for non-positive values.\")\n",
        "\n",
        "        elif choice == '8':  # Sine\n",
        "            angle = float(input(\"Enter the angle in degrees: \"))\n",
        "            print(f\"The sine of {angle} degrees is: {math.sin(math.radians(angle))}\")\n",
        "\n",
        "        elif choice == '9':  # Cosine\n",
        "            angle = float(input(\"Enter the angle in degrees: \"))\n",
        "            print(f\"The cosine of {angle} degrees is: {math.cos(math.radians(angle))}\")\n",
        "\n",
        "        elif choice == '10':  # Tangent\n",
        "            angle = float(input(\"Enter the angle in degrees: \"))\n",
        "            print(f\"The tangent of {angle} degrees is: {math.tan(math.radians(angle))}\")\n",
        "\n",
        "        elif choice == '11':  # Factorial\n",
        "            num = int(input(\"Enter an integer: \"))\n",
        "            if num >= 0:\n",
        "                print(f\"The factorial of {num} is: {math.factorial(num)}\")\n",
        "            else:\n",
        "                print(\"Error! Factorial not defined for negative numbers.\")\n",
        "\n",
        "        elif choice == '12':  # Exit\n",
        "            print(\"Exiting the calculator. Goodbye!\")\n",
        "            break\n",
        "        else:\n",
        "            print(\"Invalid input! Please enter a number between 1 and 12.\")\n",
        "\n",
        "# Run the calculator\n",
        "scientific_calculator()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "opAN6S9vjYNx",
        "outputId": "be7ead4e-99c4-4783-8f82-9f80b9ed0c48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the Scientific Calculator!\n",
            "Select the operation you want to perform:\n",
            "1. Addition (+)\n",
            "2. Subtraction (-)\n",
            "3. Multiplication (*)\n",
            "4. Division (/)\n",
            "5. Exponential (x^y)\n",
            "6. Square root (√x)\n",
            "7. Logarithm (log base 10)\n",
            "8. Sine (sin)\n",
            "9. Cosine (cos)\n",
            "10. Tangent (tan)\n",
            "11. Factorial (n!)\n",
            "12. Exit\n"
          ]
        }
      ]
    }
  ]
}
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMiIi4kDgjAsQYdui5RnO0u",
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
        "<a href=\"https://colab.research.google.com/github/mathwadde/NLP_COURSE_WORK_2026_IOW/blob/main/ILORI_WAHEED_ASSIGNIMENT_1_Part_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "uploaded = files.upload()  # A button will appear — select your dates.txt"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "id": "kGZDkPdCXW16",
        "outputId": "5bc86571-b71f-46d8-b7d5-78405535fb29"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-94e99d7f-eda8-4f02-b609-44bdc8606cee\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-94e99d7f-eda8-4f02-b609-44bdc8606cee\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving dates.txt to dates.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import re\n",
        "from datetime import datetime\n",
        "\n",
        "# Load the data\n",
        "doc = []\n",
        "with open('dates.txt') as file:\n",
        "    for line in file:\n",
        "        doc.append(line)\n",
        "\n",
        "df = pd.Series(doc)\n",
        "print(f\"Loaded {len(df)} medical notes\")\n",
        "print(\"\\nFirst 5 notes:\")\n",
        "print(df.head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3SdHICIIWoxY",
        "outputId": "7ac844f1-9dc0-4c04-ad74-6e0dd8cfebd6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Loaded 500 medical notes\n",
            "\n",
            "First 5 notes:\n",
            "0         03/25/93 Total time of visit (in minutes):\\n\n",
            "1                       6/18/85 Primary Care Doctor:\\n\n",
            "2    sshe plans to move as of 7/8/71 In-Home Servic...\n",
            "3                7 on 9/27/75 Audit C Score Current:\\n\n",
            "4    2/6/96 sleep studyPain Treatment Pain Level (N...\n",
            "dtype: object\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 1"
      ],
      "metadata": {
        "id": "rtCwPuqU1UJK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_one():\n",
        "    \"\"\"\n",
        "    Extract all dates in MM/DD/YY or MM/DD/YYYY format.\n",
        "\n",
        "    Returns:\n",
        "        list: List of matched date strings\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    pattern = r'\\b\\d{2}/\\d{2}/(\\d{2,4})\\b'  # Define your regex pattern\n",
        "\n",
        "    results = []\n",
        "    for note in df:\n",
        "        matches = re.findall(pattern, note)\n",
        "        results.extend(matches)\n",
        "\n",
        "    return results\n",
        "\n",
        "# Test your function\n",
        "q1_result = question_one()\n",
        "print(f\"Found {len(q1_result)} dates\")\n",
        "print(f\"First 10: {q1_result[:10]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_RU7J8BR1AnZ",
        "outputId": "facc01d5-085e-41b7-9cc6-9e6fd6274a33"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 34 dates\n",
            "First 10: ['93', '89', '1976', '79', '1984', '86', '1985', '91', '94', '75']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 2"
      ],
      "metadata": {
        "id": "UilRbzsgMjkD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_two():\n",
        "    \"\"\"\n",
        "    Extract all dates with month names (e.g., Mar 20, 2009).\n",
        "\n",
        "    Returns:\n",
        "        list: List of matched date strings\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    pattern = r'\\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \\d{1,2} \\d{4}\\b'\n",
        "    #pattern = r'\\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \\d{1,2}\\d{4}\\b' # Define your regex pattern\n",
        "\n",
        "    results = []\n",
        "    for note in df:\n",
        "        matches = re.findall(pattern, note)\n",
        "        results.extend(matches)\n",
        "\n",
        "    return results\n",
        "\n",
        "# Test your function\n",
        "q2_result = question_two()\n",
        "print(f\"Found {len(q2_result)} dates\")\n",
        "print(f\"First 10: {q2_result[:10]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V41TkNuYD0ui",
        "outputId": "8fe79e23-5bd7-47a3-bb54-baa61ca41ed8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 5 dates\n",
            "First 10: ['Jan 24 1986', 'October 23 1990', 'August 12 2004', 'Dec 14 1975', 'October 14 1974']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 3"
      ],
      "metadata": {
        "id": "dZCDHo7tNI6w"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_three():\n",
        "    \"\"\"\n",
        "    Extract all dates in DD Month YYYY format.\n",
        "\n",
        "    Returns:\n",
        "        list: List of matched date strings\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    pattern = r'\\b\\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \\d{4}\\b' # Define your regex pattern\n",
        "\n",
        "    results = []\n",
        "    for note in df:\n",
        "        matches = re.findall(pattern, note)\n",
        "        results.extend(matches)\n",
        "\n",
        "    return results\n",
        "\n",
        "# Test your function\n",
        "q3_result = question_three()\n",
        "print(f\"Found {len(q3_result)} dates\")\n",
        "print(f\"First 10: {q3_result[:10]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T3mHIBNANFG1",
        "outputId": "9efcad24-e81f-4185-8dd0-9200e5122ed2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 69 dates\n",
            "First 10: ['24 Jan 2001', '10 Sep 2004', '26 May 1982', '28 June 2002', '06 May 1972', '25 Oct 1987', '14 Oct 1996', '30 Nov 2007', '28 June 1994', '14 Jan 1981']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 4"
      ],
      "metadata": {
        "id": "tVE_FjQZlcvM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_four(text):\n",
        "    \"\"\"\n",
        "    Extract all email addresses from text.\n",
        "\n",
        "    Args:\n",
        "        text (str): Input text\n",
        "\n",
        "    Returns:\n",
        "        list: List of email addresses\n",
        "    \"\"\"\n",
        "    # Define your regex pattern\n",
        "    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\n",
        "\n",
        "    return re.findall(pattern, text)\n",
        "\n",
        "# Test your function\n",
        "test_text = \"\"\"\n",
        "Contact us at support@company.com or sales@company.org.\n",
        "You can also reach john.doe@email.co.uk or jane_doe123@university.edu.\n",
        "Invalid emails: @invalid.com, user@, not-an-email\n",
        "\"\"\"\n",
        "\n",
        "q4_result = question_four(test_text)\n",
        "print(f\"Found emails: {q4_result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FDR3BBmhn3ss",
        "outputId": "d769972f-9946-4ec1-93ad-52f5d0b613e6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found emails: ['support@company.com', 'sales@company.org', 'john.doe@email.co.uk', 'jane_doe123@university.edu']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 5"
      ],
      "metadata": {
        "id": "Ong_2HPVly-R"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_five(text):\n",
        "    \"\"\"\n",
        "    Clean text by removing digits, punctuation, and normalizing whitespace.\n",
        "\n",
        "    Args:\n",
        "        text (str): Input text\n",
        "\n",
        "    Returns:\n",
        "        str: Cleaned text\n",
        "    \"\"\"\n",
        "    # remove digit\n",
        "    text = re.sub(r'\\d+', '', text)\n",
        "    # remove punctuation\n",
        "    text = re.sub(r'[^\\w\\s]', '', text)\n",
        "    # normalize whitespace\n",
        "    text = re.sub(r'\\s+', ' ', text).strip()\n",
        "    # convert to lower case\n",
        "    text = text.lower()\n",
        "\n",
        "    return text  # Return cleaned text\n",
        "\n",
        "# Test your function\n",
        "test_text = \"Hello, World! 123 This is a TEST... with 456 numbers!!!\"\n",
        "q5_result = question_five(test_text)\n",
        "print(f\"Original: '{test_text}'\")\n",
        "print(f\"Cleaned:  '{q5_result}'\")\n",
        "# Expected: 'hello world this is a test with numbers'"
      ],
      "metadata": {
        "id": "3ipodEscOZwd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "569007f2-c73c-4663-e010-3ee8c9860aee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original: 'Hello, World! 123 This is a TEST... with 456 numbers!!!'\n",
            "Cleaned:  'hello world this is a test with numbers'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 6"
      ],
      "metadata": {
        "id": "2-CWQvizphn7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_six(text):\n",
        "    \"\"\"\n",
        "    Extract phone numbers and return them in XXX-XXX-XXXX format.\n",
        "\n",
        "    Args:\n",
        "        text (str): Input text\n",
        "\n",
        "    Returns:\n",
        "        list: List of phone numbers in XXX-XXX-XXXX format\n",
        "    \"\"\"\n",
        "    # Pattern to match various phone number formats\n",
        "    pattern = r'\\(?\\d{3}\\)?[\\s.\\-]\\d{3}[\\s.\\-]\\d{4}'\n",
        "\n",
        "    # Find all matches\n",
        "    matches = re.findall(pattern, text)\n",
        "\n",
        "    # Standardize each match to XXX-XXX-XXXX format\n",
        "    standardized = []\n",
        "    for match in matches:\n",
        "        # Extract only digits\n",
        "        digits = re.sub(r'\\D', '', match)\n",
        "        # Reformat to XXX-XXX-XXXX\n",
        "        formatted = f\"{digits[:3]}-{digits[3:6]}-{digits[6:]}\"\n",
        "        standardized.append(formatted)\n",
        "\n",
        "    return standardized\n",
        "\n",
        "# Test your function\n",
        "test_text = \"\"\"\n",
        "Call us at 123-456-7890 or (555) 123-4567.\n",
        "You can also reach us at 888.555.1234 or 999 888 7777.\n",
        "Invalid: 12-34-5678, 1234567890\n",
        "\"\"\"\n",
        "\n",
        "q6_result = question_six(test_text)\n",
        "print(f\"Found phones: {q6_result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YT3jBydCplaN",
        "outputId": "a49cd323-cba8-470d-a9bd-d60133b0d0e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found phones: ['123-456-7890', '555-123-4567', '888-555-1234', '999-888-7777']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 7"
      ],
      "metadata": {
        "id": "3C06aBugqToK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_seven():\n",
        "    \"\"\"\n",
        "    Extract dates from all medical notes and return indices sorted chronologically.\n",
        "\n",
        "    Returns:\n",
        "        pd.Series: Series of length 500 with original indices sorted by date\n",
        "    \"\"\"\n",
        "\n",
        "    date_patterns = [\n",
        "        # Format: 04/20/2009, 04/20/09, 4/20/09, 4/3/09\n",
        "        r'\\b(\\d{1,2})[\\/](\\d{1,2})[\\/](\\d{2,4})\\b',\n",
        "\n",
        "        # Format: Mar-20-2009, Mar 20, 2009, March 20, 2009\n",
        "        r'\\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\\s\\-](\\d{1,2})[,\\s]+(\\d{4})\\b',\n",
        "\n",
        "        # Format: 20 Mar 2009, 20 March 2009\n",
        "        r'\\b(\\d{1,2})[\\s](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\\s](\\d{4})\\b',\n",
        "\n",
        "        # Format: Mar 2009, March 2009 (no day)\n",
        "        r'\\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\\s,]+(\\d{4})\\b',\n",
        "\n",
        "        # Format: 2009 (year only)\n",
        "        r'\\b(\\d{4})\\b'\n",
        "    ]\n",
        "\n",
        "    def extract_date(text):\n",
        "        # Try each pattern in order of specificity\n",
        "\n",
        "        # MM/DD/YYYY or MM/DD/YY\n",
        "        m = re.search(date_patterns[0], text)\n",
        "        if m:\n",
        "            month, day, year = m.group(1), m.group(2), m.group(3)\n",
        "            if len(year) == 2:\n",
        "                year = '19' + year if int(year) > 25 else '20' + year\n",
        "            try:\n",
        "                return datetime.strptime(f\"{month}/{day}/{year}\", \"%m/%d/%Y\")\n",
        "            except: pass\n",
        "\n",
        "        # Month name DD, YYYY\n",
        "        m = re.search(date_patterns[1], text, re.IGNORECASE)\n",
        "        if m:\n",
        "            try:\n",
        "                return datetime.strptime(f\"{m.group(1)} {m.group(2)} {m.group(3)}\", \"%b %d %Y\")\n",
        "            except: pass\n",
        "\n",
        "        # DD Month YYYY\n",
        "        m = re.search(date_patterns[2], text, re.IGNORECASE)\n",
        "        if m:\n",
        "            try:\n",
        "                return datetime.strptime(f\"{m.group(2)} {m.group(1)} {m.group(3)}\", \"%b %d %Y\")\n",
        "            except: pass\n",
        "\n",
        "        # Month YYYY (no day — default to 1st)\n",
        "        m = re.search(date_patterns[3], text, re.IGNORECASE)\n",
        "        if m:\n",
        "            try:\n",
        "                return datetime.strptime(f\"{m.group(1)} {m.group(2)}\", \"%b %Y\")\n",
        "            except: pass\n",
        "\n",
        "        # Year only — default to Jan 1st\n",
        "        m = re.search(date_patterns[4], text)\n",
        "        if m:\n",
        "            year = int(m.group(1))\n",
        "            if 1900 <= year <= 2100:\n",
        "                try:\n",
        "                    return datetime(year, 1, 1)\n",
        "                except: pass\n",
        "\n",
        "        return None  # No date found\n",
        "\n",
        "    # Extract dates from all notes in df\n",
        "    dates = df.map(extract_date)\n",
        "\n",
        "    # Sort indices by date chronologically\n",
        "    sorted_indices = dates.sort_values().index\n",
        "\n",
        "    return pd.Series(sorted_indices)\n",
        "\n",
        "\n",
        "# Test your function\n",
        "q7_result = question_seven()\n",
        "print(f\"Result length: {len(q7_result)}\")\n",
        "print(f\"First 10 indices: {list(q7_result.head(10))}\")\n",
        "print(f\"Last 10 indices: {list(q7_result.tail(10))}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HwzlTJpSqTXs",
        "outputId": "c41a4136-7bf6-45f7-c70d-de4402db0e2b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result length: 500\n",
            "First 10 indices: [9, 84, 2, 53, 28, 474, 153, 13, 129, 98]\n",
            "Last 10 indices: [161, 25, 39, 40, 71, 99, 466, 470, 481, 493]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Run this cell to verify all functions exist and return correct types\n",
        "print(\"Checking functions...\")\n",
        "\n",
        "try:\n",
        "    r1 = question_one()\n",
        "    assert isinstance(r1, list), \"question_one should return a list\"\n",
        "    print(\"✓ question_one: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_one: {e}\")\n",
        "\n",
        "try:\n",
        "    r2 = question_two()\n",
        "    assert isinstance(r2, list), \"question_two should return a list\"\n",
        "    print(\"✓ question_two: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_two: {e}\")\n",
        "\n",
        "try:\n",
        "    r3 = question_three()\n",
        "    assert isinstance(r3, list), \"question_three should return a list\"\n",
        "    print(\"✓ question_three: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_three: {e}\")\n",
        "\n",
        "try:\n",
        "    r4 = question_four(\"test@email.com\")\n",
        "    assert isinstance(r4, list), \"question_four should return a list\"\n",
        "    print(\"✓ question_four: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_four: {e}\")\n",
        "\n",
        "try:\n",
        "    r5 = question_five(\"Hello World 123\")\n",
        "    assert isinstance(r5, str), \"question_five should return a string\"\n",
        "    print(\"✓ question_five: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_five: {e}\")\n",
        "\n",
        "try:\n",
        "    r6 = question_six(\"123-456-7890\")\n",
        "    assert isinstance(r6, list), \"question_six should return a list\"\n",
        "    print(\"✓ question_six: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_six: {e}\")\n",
        "\n",
        "try:\n",
        "    r7 = question_seven()\n",
        "    assert isinstance(r7, pd.Series), \"question_seven should return a pandas Series\"\n",
        "    print(\"✓ question_seven: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_seven: {e}\")\n",
        "\n",
        "print(\"\\nDone! Export this notebook as .py file when all functions pass.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a0b-hkxwrcn9",
        "outputId": "40ddb894-4dba-4f4d-f2ac-729e47bafba7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Checking functions...\n",
            "✓ question_one: OK\n",
            "✓ question_two: OK\n",
            "✓ question_three: OK\n",
            "✓ question_four: OK\n",
            "✓ question_five: OK\n",
            "✓ question_six: OK\n",
            "✓ question_seven: OK\n",
            "\n",
            "Done! Export this notebook as .py file when all functions pass.\n"
          ]
        }
      ]
    }
  ]
}
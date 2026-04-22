{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXjf+MA9D5rxNidQ7Wct3O",
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
        "<a href=\"https://colab.research.google.com/github/mathwadde/NLP_COURSE_WORK_2026_IOW/blob/main/ILORI_WAHEED_assignment1_part2_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "PtFRjUn_s0aQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "uploaded = files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "id": "OQOCWSeCs9I0",
        "outputId": "69d89a85-f551-40c9-daa2-6dbbe7bf640b"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-f82b4127-6fbf-450b-961e-29b5bd7f28da\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-f82b4127-6fbf-450b-961e-29b5bd7f28da\">\n",
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
            "Saving moby.txt to moby.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import re\n",
        "\n",
        "# Download required NLTK data\n",
        "nltk.download('punkt', quiet=True)\n",
        "nltk.download('punkt_tab', quiet=True)\n",
        "nltk.download('stopwords', quiet=True)\n",
        "nltk.download('wordnet', quiet=True)\n",
        "nltk.download('averaged_perceptron_tagger', quiet=True)\n",
        "nltk.download('averaged_perceptron_tagger_eng', quiet=True)\n",
        "\n",
        "from nltk.tokenize import word_tokenize, sent_tokenize\n",
        "from nltk.stem import PorterStemmer, WordNetLemmatizer\n",
        "from nltk.corpus import stopwords\n",
        "\n",
        "# Load the novel\n",
        "with open('moby.txt', 'r') as f:\n",
        "    moby_raw = f.read()\n",
        "\n",
        "# Create NLTK Text object\n",
        "moby_tokens = nltk.word_tokenize(moby_raw)\n",
        "text1 = nltk.Text(moby_tokens)\n",
        "\n",
        "print(f\"Loaded Moby Dick\")\n",
        "print(f\"Raw text length: {len(moby_raw)} characters\")\n",
        "print(f\"First 200 characters: {moby_raw[:200]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3spWkEdNsYMi",
        "outputId": "e4072f3c-c8d7-4ee3-dfc8-37a10be668d9"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Loaded Moby Dick\n",
            "Raw text length: 1220066 characters\n",
            "First 200 characters: [Moby Dick by Herman Melville 1851]\n",
            "\n",
            "\n",
            "ETYMOLOGY.\n",
            "\n",
            "(Supplied by a Late Consumptive Usher to a Grammar School)\n",
            "\n",
            "The pale Usher--threadbare in coat, heart, body, and brain; I see him\n",
            "now.  He was ever du\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Example 1: Count total tokens\n",
        "def example_one():\n",
        "    return len(nltk.word_tokenize(moby_raw))\n",
        "\n",
        "print(f\"Total tokens: {example_one()}\")\n",
        "\n",
        "# Example 2: Count unique tokens\n",
        "def example_two():\n",
        "    return len(set(nltk.word_tokenize(moby_raw)))\n",
        "\n",
        "print(f\"Unique tokens: {example_two()}\")\n",
        "\n",
        "# Example 3: Lemmatize verbs and count unique\n",
        "def example_three():\n",
        "    lemmatizer = WordNetLemmatizer()\n",
        "    lemmatized = [lemmatizer.lemmatize(w, 'v') for w in text1]\n",
        "    return len(set(lemmatized))\n",
        "\n",
        "print(f\"Unique tokens after verb lemmatization: {example_three()}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9HRxo22uuxO5",
        "outputId": "46563f6a-db4f-466c-b135-db9b593a0bc1"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total tokens: 255222\n",
            "Unique tokens: 20639\n",
            "Unique tokens after verb lemmatization: 16908\n"
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
        "id": "ohZelUngugQN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_one():\n",
        "    \"\"\"\n",
        "    Calculate the lexical diversity of the text.\n",
        "\n",
        "    Returns:\n",
        "        float: Ratio of unique tokens to total tokens\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    unique_tokens = len(set(text1))\n",
        "    total_tokens = len(text1)\n",
        "    lexical_diversity = unique_tokens / total_tokens\n",
        "    return lexical_diversity\n",
        "\n",
        "    return None\n",
        "\n",
        "# Test your function\n",
        "q1_result = question_one()\n",
        "print(f\"Lexical diversity: {q1_result}\")\n",
        "# Expected: approximately 0.08 (8%)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j53Td_B8tkld",
        "outputId": "af96120c-8d60-4ba2-a093-0d3526a49ca2"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lexical diversity: 0.08086685317096488\n"
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
        "id": "3aaUu17Mv5f2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_two():\n",
        "    \"\"\"\n",
        "    Calculate the percentage of tokens that are 'whale' or 'Whale'.\n",
        "\n",
        "    Returns:\n",
        "        float: Percentage of whale tokens\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    whale_tokens = [w for w in text1 if re.search(r'^[Ww]hale$', w)]\n",
        "    total_tokens = len(text1)\n",
        "    whale_percentage = (len(whale_tokens) / total_tokens)*100\n",
        "    return whale_percentage\n",
        "\n",
        "\n",
        "# Test your function\n",
        "q2_result = question_two()\n",
        "print(f\"Percentage of 'whale'/'Whale': {q2_result}%\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "33CYdEXcufuH",
        "outputId": "08290d14-04d8-47f7-d07d-ee95442c98c8"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percentage of 'whale'/'Whale': 0.41571651346670746%\n"
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
        "id": "WbHEdJ8hwwUE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_three():\n",
        "    \"\"\"\n",
        "    Find the 20 most frequent tokens and their frequencies.\n",
        "\n",
        "    Returns:\n",
        "        list: List of 20 tuples (token, frequency) sorted by frequency descending\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    # Hint: Use nltk.FreqDist\n",
        "    freq_dist = nltk.FreqDist(text1)\n",
        "    most_common_20 = freq_dist.most_common(20)\n",
        "    return most_common_20\n",
        "\n",
        "\n",
        "# Test your function\n",
        "q3_result = question_three()\n",
        "print(\"20 most frequent tokens:\")\n",
        "for token, freq in q3_result:\n",
        "    print(f\"  {token}: {freq}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1KSRLLf_w19V",
        "outputId": "c9f38355-4678-4156-a4d6-1ef48e244999"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20 most frequent tokens:\n",
            "  ,: 19204\n",
            "  the: 13715\n",
            "  .: 7306\n",
            "  of: 6513\n",
            "  and: 6010\n",
            "  a: 4545\n",
            "  to: 4515\n",
            "  ;: 4173\n",
            "  in: 3908\n",
            "  that: 2981\n",
            "  his: 2459\n",
            "  it: 2206\n",
            "  I: 2121\n",
            "  !: 1767\n",
            "  's: 1731\n",
            "  is: 1722\n",
            "  --: 1713\n",
            "  he: 1660\n",
            "  with: 1659\n",
            "  was: 1640\n"
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
        "id": "J4WN9cblySaK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_four():\n",
        "    \"\"\"\n",
        "    Find tokens with length > 5 and frequency > 150.\n",
        "\n",
        "    Returns:\n",
        "        list: Alphabetically sorted list of tokens\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    token_freq = nltk.FreqDist(text1)\n",
        "    token_leng = [token for token, freq in token_freq.items() if len(token) > 5 and freq > 150]\n",
        "    token_leng.sort()\n",
        "    return token_leng\n",
        "\n",
        "# Test your function\n",
        "q4_result = question_four()\n",
        "print(f\"Found {len(q4_result)} tokens:\")\n",
        "print(q4_result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "htmctkj9yVed",
        "outputId": "ab4c01b3-0fe4-469c-aa89-67ca2ee59e3b"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 14 tokens:\n",
            "['Captain', 'Pequod', 'Queequeg', 'Starbuck', 'almost', 'before', 'himself', 'little', 'seemed', 'should', 'though', 'through', 'whales', 'without']\n"
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
        "id": "g_4cmPMWz5x_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_five():\n",
        "    \"\"\"\n",
        "    Find the longest word in the text.\n",
        "\n",
        "    Returns:\n",
        "        tuple: (longest_word, length)\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    longest_word = max(text1, key=len)\n",
        "    return (longest_word, len(longest_word))\n",
        "\n",
        "    return (None, 0)\n",
        "\n",
        "# Test your function\n",
        "q5_result = question_five()\n",
        "print(f\"Longest word: '{q5_result[0]}' with length {q5_result[1]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NXbhs4Cgz7w_",
        "outputId": "7353ab01-a2d1-4216-891d-55eece70ffc4"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Longest word: 'twelve-o'clock-at-night' with length 23\n"
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
        "id": "n65Qqywx0VKh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_six():\n",
        "    \"\"\"\n",
        "    Find words with frequency > 2000.\n",
        "\n",
        "    Returns:\n",
        "        list: List of tuples (frequency, word) sorted by frequency descending\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    token_freq = nltk.FreqDist(text1)\n",
        "    freq_words = [(freq, token) for token, freq in token_freq.items() if freq > 2000]\n",
        "    freq_words.sort(reverse=True)\n",
        "    return freq_words\n",
        "\n",
        "\n",
        "# Test your function\n",
        "q6_result = question_six()\n",
        "print(\"Words with frequency > 2000:\")\n",
        "for freq, word in q6_result:\n",
        "    print(f\"  {word}: {freq}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gmzp_eDVznu9",
        "outputId": "689dedb8-8fef-49fa-85da-a41302c9bb64"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Words with frequency > 2000:\n",
            "  ,: 19204\n",
            "  the: 13715\n",
            "  .: 7306\n",
            "  of: 6513\n",
            "  and: 6010\n",
            "  a: 4545\n",
            "  to: 4515\n",
            "  ;: 4173\n",
            "  in: 3908\n",
            "  that: 2981\n",
            "  his: 2459\n",
            "  it: 2206\n",
            "  I: 2121\n"
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
        "id": "oR6VD4F60xjW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_seven():\n",
        "    \"\"\"\n",
        "    Calculate the average number of tokens per sentence.\n",
        "\n",
        "    Returns:\n",
        "        float: Average tokens per sentence\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    # Hint: Use sent_tokenize for sentences, word_tokenize for words\n",
        "    sentences = sent_tokenize(moby_raw)\n",
        "    words = word_tokenize(moby_raw)\n",
        "    avg_tokens_per_sentence = len(words) / len(sentences)\n",
        "    return avg_tokens_per_sentence\n",
        "\n",
        "# Test your function\n",
        "q7_result = question_seven()\n",
        "print(f\"Average tokens per sentence: {q7_result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tCxHhEic01hR",
        "outputId": "5db84096-bef9-4e48-9c96-4a359dbeba5f"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Average tokens per sentence: 25.90560292326431\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Queation 8"
      ],
      "metadata": {
        "id": "6I6CQeMG1XuH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_eight():\n",
        "    \"\"\"\n",
        "    Find 10 most common words after removing stop words.\n",
        "\n",
        "    Returns:\n",
        "        list: List of 10 tuples (word, frequency) sorted by frequency descending\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    # Hint: Use stopwords.words('english')\n",
        "    stop_words = set(stopwords.words('english'))\n",
        "    filtered_words = [word for word in text1 if word.lower() not in stop_words]\n",
        "    freq_dist = nltk.FreqDist(filtered_words)\n",
        "    most_common_10 = freq_dist.most_common(10)\n",
        "    return most_common_10\n",
        "\n",
        "\n",
        "# Test your function\n",
        "q8_result = question_eight()\n",
        "print(\"10 most common words (excluding stop words):\")\n",
        "for word, freq in q8_result:\n",
        "    print(f\"  {word}: {freq}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b-DFl8Fl1dVD",
        "outputId": "1ddd6d96-be1e-4f3f-e0df-ade3378bb0f4"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 most common words (excluding stop words):\n",
            "  ,: 19204\n",
            "  .: 7306\n",
            "  ;: 4173\n",
            "  !: 1767\n",
            "  's: 1731\n",
            "  --: 1713\n",
            "  '': 1615\n",
            "  ``: 1456\n",
            "  ?: 1004\n",
            "  one: 881\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 9"
      ],
      "metadata": {
        "id": "8i-Cwxs-2Lr3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_nine():\n",
        "    \"\"\"\n",
        "    Find 10 most common stems using Porter stemmer.\n",
        "\n",
        "    Returns:\n",
        "        list: List of 10 tuples (stem, frequency) sorted by frequency descending\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    porter_stemmer = PorterStemmer()\n",
        "    stemmed_words = [porter_stemmer.stem(word) for word in text1]\n",
        "    freq_dist = nltk.FreqDist(stemmed_words)\n",
        "    most_common_10 = freq_dist.most_common(10)\n",
        "    return most_common_10\n",
        "\n",
        "\n",
        "\n",
        "# Test your function\n",
        "q9_result = question_nine()\n",
        "print(\"10 most common stems:\")\n",
        "for stem, freq in q9_result:\n",
        "    print(f\"  {stem}: {freq}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1zwhN3zh2Sde",
        "outputId": "3f2aaed3-35f9-4167-9886-bbd1a0cf9241"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 most common stems:\n",
            "  ,: 19204\n",
            "  the: 14422\n",
            "  .: 7306\n",
            "  of: 6590\n",
            "  and: 6421\n",
            "  a: 4698\n",
            "  to: 4597\n",
            "  ;: 4173\n",
            "  in: 4163\n",
            "  that: 3084\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 10"
      ],
      "metadata": {
        "id": "gNNI2MQv55as"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def question_ten():\n",
        "    \"\"\"\n",
        "    Preprocess the first 1000 characters of Moby Dick.\n",
        "\n",
        "    Returns:\n",
        "        list: List of preprocessed tokens\n",
        "    \"\"\"\n",
        "    text = moby_raw[:1000]\n",
        "    stop_words = set(stopwords.words('english'))\n",
        "    lemmatizer = WordNetLemmatizer()\n",
        "\n",
        "    # YOUR CODE HERE\n",
        "    # Steps:\n",
        "    # 1. Tokenize\n",
        "    tokens = nltk.word_tokenize(text)\n",
        "    # 2. Lowercase\n",
        "    tokens = [token.lower() for token in tokens]\n",
        "    # 3. Keep only alphabetic tokens\n",
        "    tokens = [token for token in tokens if token.isalpha()]\n",
        "    # 4. Remove stop words\n",
        "    tokens = [token for token in tokens if token not in stop_words]\n",
        "    # 5. Lemmatize\n",
        "    tokens = [lemmatizer.lemmatize(token) for token in tokens]\n",
        "\n",
        "    return tokens\n",
        "\n",
        "\n",
        "# Test your function\n",
        "q10_result = question_ten()\n",
        "print(f\"Number of preprocessed tokens: {len(q10_result)}\")\n",
        "print(f\"First 20 tokens: {q10_result[:20]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FnfWDZFu52xa",
        "outputId": "9d5cc75d-12e5-425f-bc2d-a20543134a03"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of preprocessed tokens: 85\n",
            "First 20 tokens: ['moby', 'dick', 'herman', 'melville', 'etymology', 'supplied', 'late', 'consumptive', 'usher', 'grammar', 'school', 'pale', 'usher', 'threadbare', 'coat', 'heart', 'body', 'brain', 'see', 'ever']\n"
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
        "    assert isinstance(r1, float), \"question_one should return a float\"\n",
        "    print(\"✓ question_one: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_one: {e}\")\n",
        "\n",
        "try:\n",
        "    r2 = question_two()\n",
        "    assert isinstance(r2, float), \"question_two should return a float\"\n",
        "    print(\"✓ question_two: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_two: {e}\")\n",
        "\n",
        "try:\n",
        "    r3 = question_three()\n",
        "    assert isinstance(r3, list) and len(r3) == 20, \"question_three should return a list of 20 tuples\"\n",
        "    print(\"✓ question_three: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_three: {e}\")\n",
        "\n",
        "try:\n",
        "    r4 = question_four()\n",
        "    assert isinstance(r4, list), \"question_four should return a list\"\n",
        "    print(\"✓ question_four: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_four: {e}\")\n",
        "\n",
        "try:\n",
        "    r5 = question_five()\n",
        "    assert isinstance(r5, tuple) and len(r5) == 2, \"question_five should return a tuple of 2 elements\"\n",
        "    print(\"✓ question_five: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_five: {e}\")\n",
        "\n",
        "try:\n",
        "    r6 = question_six()\n",
        "    assert isinstance(r6, list), \"question_six should return a list\"\n",
        "    print(\"✓ question_six: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_six: {e}\")\n",
        "\n",
        "try:\n",
        "    r7 = question_seven()\n",
        "    assert isinstance(r7, float), \"question_seven should return a float\"\n",
        "    print(\"✓ question_seven: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_seven: {e}\")\n",
        "\n",
        "try:\n",
        "    r8 = question_eight()\n",
        "    assert isinstance(r8, list) and len(r8) == 10, \"question_eight should return a list of 10 tuples\"\n",
        "    print(\"✓ question_eight: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_eight: {e}\")\n",
        "\n",
        "try:\n",
        "    r9 = question_nine()\n",
        "    assert isinstance(r9, list) and len(r9) == 10, \"question_nine should return a list of 10 tuples\"\n",
        "    print(\"✓ question_nine: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_nine: {e}\")\n",
        "\n",
        "try:\n",
        "    r10 = question_ten()\n",
        "    assert isinstance(r10, list), \"question_ten should return a list\"\n",
        "    print(\"✓ question_ten: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_ten: {e}\")\n",
        "\n",
        "print(\"\\nDone! Export this notebook as .py file when all functions pass.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "83NCuIGM6dGp",
        "outputId": "a291052a-3f65-428b-e189-068b68ed0bbb"
      },
      "execution_count": 26,
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
            "✓ question_eight: OK\n",
            "✓ question_nine: OK\n",
            "✓ question_ten: OK\n",
            "\n",
            "Done! Export this notebook as .py file when all functions pass.\n"
          ]
        }
      ]
    }
  ]
}
# llm_access

[![License](https://img.shields.io/badge/license-Custom--SA-%231b25e5)](https://raw.githubusercontent.com/Python-Components-Group/llm_access/refs/heads/master/LICENSE)

A Python component for integrating LLMs into any sort of Python software system, abstracting on:
    - Inference platform used
    - Platform-specific LLM models implementation names
    - Platform-specific/Model-specific LLM hyperparameters
(mainly used in [GenTestsAILib](https://github.com/codesavant23/gentestsai/))

## Component Description

This Python component is built by several sub-components (or software modules):
- **<u>llm_api</u>** which describes implemented inference platforms
- **<u>llm_chat</u>** which provides services related to chat objects
- **<u>llm_specimpl</u>** which provides abstraction over LLMs specific implementations  
- **<u>llm_hyperparam</u>** which provides abstraction over LLMs hyperparameters
- **<u>llm_apiaccessor</u>** which provides services for communicating with LLMs exposed by an inference platform abstractly

## How to get the component

### Latest stable release

You can find the binaries of the component in the [release](https://github.com/Python-Components-Group/llm_access/releases) section of this repository

### Latest build

#### Installation

  ```python
  pip install git+https://github.com/Python-Components-Group/llm_access
  ```

#### Update

  ```python
  pip install git+https://github.com/Python-Components-Group/llm_access --upgrade
  ```


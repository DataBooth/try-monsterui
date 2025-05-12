# `try-monsterui`

- [`try-monsterui`](#try-monsterui)
  - [Status](#status)
  - [MonsterUI Framework](#monsterui-framework)
  - [App Description](#app-description)

## Status

![Status: Experimental](https://img.shields.io/badge/status-experimental-orange.svg)


*The [MonsterUI](https://monsterui.answer.ai) package continues to evolve rapidly, as does the underlying [FastHTML](https://www.fastht.ml) package. The goal is to provide a simple and effective way to create web UIs using Python, with a focus on ease of use and flexibility. The API is likely to change frequently as new features are added and existing ones are refined. I typically use [Streamlit](https://streamlit.io) for my data app projects, but I wanted to explore the potential of MonsterUI and FastHTML for creating more customisable web applications.*

Note that these experiment were run in mid-February 2025 and are probably outdated -- a re-visit in late 2025 is worthwhile.

## MonsterUI Framework

MonsterUI is a Python library designed to streamline the creation of web UIs using FastHTML. It provides a set of pre-designed components and styling options that allow developers to quickly build attractive and functional interfaces. Key features of MonsterUI include:

*   **Theming**: Easily apply consistent visual styles using predefined themes.
*   **Pre-built Components**: A wide range of UI elements like NavBars, Cards, Modals, Buttons, and more.
*   **Layout Tools**: Components for structuring content, such as Containers, Grids, and Flexbox utilities.
*   **DaisyUI Integration**: Uses DaisyUI for Tailwind CSS styling.
*   **FastHTML Compatibility**: Works seamlessly with FastHTML for generating HTML structures.

The aim of the MonsterUI framework is to allow developers to focus on the logic and content of applications, relying on the framework to handle much of the UI styling and layout.

## App Description

The initial app consists of a main page, two additional pages (Page 1 and Page 2), a navigation bar for easy movement between pages, a toggleable sidebar on the main page for additional navigation, and an initial splash screen presented as a modal to welcome users. The goal is to create a structured and visually appealing user interface with minimal custom JavaScript.
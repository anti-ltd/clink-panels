<p align="center">
  <img src="https://raw.githubusercontent.com/anti-ltd/clink-language-packs/main/icon-1024.png" width="96" alt="Clink app icon">
</p>

<h1 align="center">Clink panels</h1>

<p align="center">Open custom keyboard panels for Clink.</p>

Panels replace the keyboard with a focused tool, such as a snippet board, character picker, or utility. They contain constrained panel logic and download only after the person using Clink explicitly trusts the repository.

## Official Clink repositories

[Language packs](https://github.com/anti-ltd/clink-language-packs) · [Layouts](https://github.com/anti-ltd/clink-layouts) · [Profiles](https://github.com/anti-ltd/clink-profiles) · [Themes](https://github.com/anti-ltd/clink-themes) · [Panels](https://github.com/anti-ltd/clink-panels) · [Actions](https://github.com/anti-ltd/clink-actions) · [Fonts](https://github.com/anti-ltd/clink-fonts) · [Sounds](https://github.com/anti-ltd/clink-sounds)

## Included panels

The official repository currently includes:

| Panel | What it does |
|---|---|
| Kaomoji | Inserts expressive text faces. |
| Snippets | Keeps frequently used text close to the keyboard. |
| Fonts | Converts selected text into decorative Unicode styles. |

The files live in [`Panels/`](Panels). They are small and readable, so they are a good place to start when making your own.

## Make your first panel

1. Fork this repository.
2. Copy a file in [`Panels/`](Panels), rename it, and change its visible name and summary.
3. Test it in Clink by importing the file before publishing.
4. Run the repository validation tools if they are present.
5. Push to `main`. GitHub Actions publishes the panels and manifest to the `latest` release.

## Add your repository to Clink

Open **General → Repositories** in Clink and add `owner/repository`. Then open **Tools → Custom Panels** and choose your repository. Clink asks for a separate trust decision before downloading panel logic.

## What Clink verifies

Clink accepts only public HTTPS GitHub release files from the repository you added. It verifies the manifest, SHA-256 hash, byte count, file type, and constrained source policy before installation.

Panels contain executable-style logic, so adding a repository is a stronger trust decision than adding data-only packs. Only add repositories whose code and release process you trust.

## Publishing is automatic

Keep `Panels/`, `tools/`, and `.github/workflows/` in your fork. Add or update a panel and push to `main`. GitHub Actions validates the files and refreshes the `latest` release.

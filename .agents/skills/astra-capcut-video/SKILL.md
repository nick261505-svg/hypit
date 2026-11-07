---
name: astra-capcut-video
description: Create short videos from a reference URL or file with reference analysis, narration, matching captions, and an editable CapCut project; export an MP4 only when requested. Use for video production or localization; not for analysis-only requests.
---

# CapCut short video

For GloPick narration, start with the [natural animal-story narration guide](references/sbs-animal-conversational-narration.md): conversational Korean, a question or observation that opens curiosity, scene-specific facts, short reactions, and a visible resolution. Use the [TJB swan news analysis](references/tjb-swan-narration.md) only as an optional pacing reference. The reference broadcasts' wording, voice recordings, graphics, music, and footage are not production sources. Write a new, fact-checked hook and narration for each story.

Use this skill when the user commissions a finished video or an editable CapCut project. The current model can direct production; invoking a skill does not switch models. For GloPick shorts, use the user's [channel layout](references/glopick-layout.md) and apply the [source-rights and original-contribution gate](references/glopick-rights.md) from candidate selection through publication review. An edited or narrated source clip is not automatically cleared for reuse.

The workflow in [source analysis](references/source-analysis.md) is an example of the production pattern. It does not include the presenter's private Gems, chat history, TTS account, prompt, or CapCut template. Build from the user's own brief and reusable assets. Do not claim to reproduce the exact preset shown in the video.

## Start from the commission

Determine the reference URL or file, intended audience and topic, target length and aspect ratio, language, desired voice, available source footage, style references, output folder, and whether an editable CapCut project is required. Reuse the user's established preferences and files. Ask only for missing facts that materially change production, such as voice rights or access to a required account. Keep a concise production brief beside the project. After the user accepts a result, save the reusable voice, caption, pacing, and template choices as a project preset so a later URL-only request can use them.

If the user only wants analysis, use the installed Hypit skill's reference-video method and stop at a timecoded analysis. For production, analyze the reference and explain which hook, pacing, narration, caption, B-roll, sound, and reveal relationships will be retained or changed. Use the Hypit CLI for URL download, probing, frames, and grids when available. A transcript is evidence to check against picture and audio, not a substitute for watching the reference.

## Produce the target

1. Write up to three distinct script options when a reference or user preference warrants a choice. Ground factual claims in supplied or verified sources. Identify copied footage, music, faces, and voices whose use requires the user's rights or permission. Select or ask the user to select a direction when the difference matters.
2. Turn the selected script into a shot and sound plan: narration lines, matching source ranges or licensed visuals, caption text and timing, effects, music, and expected duration. Lower captions must follow the spoken narration instead of summarizing the scene. Split long sentences into readable, timed phrases. Record asset provenance and the intended editor project name.
3. Check CapCut, the chosen TTS service, and needed local tools in the actual environment. Use an existing approved template and voice when supplied. For a paid service, show the account and expected cost or budget before calling it. Do not invent credentials or a service. Create and listen to the narration before timing the edit.
4. Prepare the actual media, narration, captions, transitions, and effects for an editable CapCut project. Never take control of the user's active Windows desktop or use computer-use automation to operate CapCut by default: this can block their mouse and keyboard. Prepare reviewable files and CapCut editing steps first. Only operate CapCut in a dedicated hands-off session if the user explicitly requests desktop control after being told that their input may be temporarily unavailable. If the user reports lost input or ends the session, stop computer-use actions immediately; do not ask them to press Esc while input is blocked. A verified project template or documented editing library can be used without desktop control, but do not edit opaque project files by guessing their schema. If CapCut UI access is unavailable, hand the prepared assets and specific steps to the user instead of claiming the project or export was verified. Do not export this user's CapCut project unless they explicitly request an export in a later message.
5. Watch and listen to the exported result when available. Check narration against captions, cut timing, text readability (especially unwanted three-line captions), B-roll relevance, audio continuity and clipping, and the opening and ending. Inspect selected source footage for embedded text, donation prompts, or subtitles that conflict with the new edit. Prefer clean source ranges; if essential footage contains text, hide it with the white layout area or a localized blur and verify the export. Keep required creator credit legible. Correct concrete defects and report which project and export checks were actually completed.

For localization, duplicate the accepted project, translate for natural speech, generate a permitted target-language voice, retime captions and edits, and inspect the localized export. Make currency, units, names, and cultural changes explicit in the brief. Do not publish or schedule uploads unless the user asks.

Keep generated media and intermediate files organized in the project folder so another session can resume. Report which parts were automated, which assets or settings were provided by the user, and any remaining manual adjustments.

## Reference

- [30:00 onward source analysis](references/source-analysis.md) — read when reproducing or adapting the pattern demonstrated in the supplied YouTube video.

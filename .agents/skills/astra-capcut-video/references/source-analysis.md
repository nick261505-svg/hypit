# Source pattern: YouTube video from 30:00 onward

Source: https://www.youtube.com/watch?v=dmBfiGigRfY&t=1800s (54:37 total). This account is based on the downloaded Korean auto-captions and sampled frames from 30:00 onward. Auto-captions may mishear product names and exact instructions; verify uncertain details on screen before treating them as requirements.

| Original time | Demonstrated step | Implication for this skill |
| --- | --- | --- |
| 30:00–32:30 | Select an older reference video with strong historical response using vidIQ trend information. | Treat popularity as one signal; inspect the source content and rights. |
| 32:30–33:40 | Paste the reference link into a custom Gemini Gem that proposes three rewritten scripts; select one. Presenter says the Gem was configured with private team messages. | Offer script variants from the user's own brief and examples; private Gem instructions are unavailable. |
| 33:40–34:40 | Paste the selected script and video link into a Codex session using Astra. Agent starts a new editing project and plans cuts and captions. | Keep source URL, approved script, edit plan, and project path together. |
| 34:40–40:20 | Astra operates a TTS site and CapCut, adjusts voice speed and trims, arranges narration and captions, checks footage, and saves an editable project. Presenter reports a roughly 61-second result after 19 minutes of work. | Make TTS and editor connections explicit; verify the real saved project rather than assuming automation succeeded. Time is one example, not a performance guarantee. |
| 40:20–42:20 | Presenter manually corrects a caption wrapping into three lines and reviews the exported short with sound. | Include human-visible QA and re-export after fixes. |
| 42:20–46:40 | Existing Korean CapCut project is copied and localized to Japanese. Presenter specifies VoiceVox for Japanese TTS; Astra checks captions, pauses, levels, and project state. | Localize from an accepted project; do not hardcode a voice or currency conversion. |
| 46:40–49:40 | Presenter shows a separate custom desktop preset app that accepts a video URL and is connected to ChatGPT, then exports MP4 or opens an editor. | That application and its presets are not part of this skill and are not available from the video. |
| 50:00–51:40 | A separate Telegram-to-other-computer workflow schedules a YouTube upload. | Upload is a distinct, optional operation outside this video creation skill. |

The visible demonstration shows Astra as a computer-using agent coordinating script, speech, and editor work. It does not show Astra generating raw video frames by itself. The reusable method is a combination of reference analysis, authored script, asset and voice preparation, editable timeline assembly, and review.

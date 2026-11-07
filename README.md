# 글로픽 동물 쇼츠 제작 스킬

Codex에서 글로픽(GloPick) 동물 쇼츠의 소재 탐색, 단일 사건 영상, 여러 사건 모음 영상을 제작할 때 쓰는 프로젝트 스킬입니다.

| 스킬 | 용도 |
| --- | --- |
| [`glopick-animal-scout`](.agents/skills/glopick-animal-scout/SKILL.md) | 원본·화질·권리 확인을 거쳐 동물 영상 소재 선정 |
| [`astra-capcut-video`](.agents/skills/astra-capcut-video/SKILL.md) | 내레이션과 SRT 자막을 갖춘 단일 사건 CapCut 쇼츠 제작 |
| [`glopick-animal-montage`](.agents/skills/glopick-animal-montage/SKILL.md) | 서로 다른 동물 영상 여러 편을 한 주제로 엮는 쇼츠 제작 |

각 스킬의 `references/`도 함께 들어 있습니다. `assets/gold_logo_transparent_1x1.png`는 글로픽 상단 프레임에 쓰는 로고입니다.

## 다른 컴퓨터에서 사용

1. 이 저장소를 복제하고 **복제한 폴더를 Codex 작업 폴더로 엽니다.** `.agents/skills/` 아래 세 스킬이 함께 로드됩니다.
2. 기존 작업 폴더에서 사용하려면 복제한 저장소의 `.agents/skills/` 아래 세 디렉터리를 기존 작업 폴더의 `.agents/skills/`로 복사합니다. `references/`를 빠뜨리지 마세요.
3. CapCut에서 기존 글로픽 프레임을 그대로 쓰려면, 별도로 보관 중인 **백조 구조 60초 쇼츠 CapCut 프로젝트**와 사용 가능한 원본 영상을 새 컴퓨터로 옮깁니다. 프로젝트 파일은 이 저장소에 포함하지 않았습니다.
4. 필요한 프로그램은 작업에 따라 CapCut, FFmpeg, 영상 확인 도구, 사용 허가된 TTS 도구입니다. Hypit CLI를 이용한 URL 분석은 선택 사항이며, 필요하면 [Hypit 원본 저장소](https://github.com/hypit-ai/hypit)의 설치 안내를 따릅니다. 스킬만 복제해도 해당 프로그램이나 계정이 자동 설치되지는 않습니다.

Windows PowerShell에서 복제하는 예:

```powershell
git clone https://github.com/nick261505-svg/hypit.git GloPick-Skills
```

## 제작 기준

- 유튜브 검색의 `필터 → 크리에이티브 커먼즈`로 후보를 찾되, **각 영상 설명의 CC BY 표기와 원 촬영자**를 다시 확인합니다. 삽입 음악 등 별도 권리도 확인합니다.
- 인스타그램 릴스와 일반 유튜브 영상은 별도 사용 허가가 없으면 참고 자료로만 씁니다.
- 실제 사용 가능한 영상 컷을 확보하기 전에 빈 화면 자리 표시 프로젝트를 완성본으로 전달하지 않습니다.
- 글로픽 단일 사건 영상은 흰 상하단, 로고와 영문·한글 채널명, 제목, 말한 내용과 맞는 한두 줄 자막을 기본으로 합니다.
- 사용자의 Windows 마우스·키보드를 점유하는 CapCut 데스크톱 자동화와 MP4 내보내기는 기본 작업에 포함되지 않습니다.

스킬 문서는 작업 방식과 기준입니다. 원본 동영상, CapCut 프로젝트, 유료 서비스 계정, API 키, 게시 권한은 이 저장소에 포함하지 않습니다.

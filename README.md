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
3. 캡컷 프로젝트도 필요하면 아래 **이동용 글로픽 60초 템플릿**을 설치합니다. 기존 백조 편집본의 흰 상하단, 로고·영문/한글 채널명, 제목, 하단 자막 구조를 가진 프로젝트입니다. 영상 트랙은 교체용 회색 컷이며 원본 영상이나 완성 영상이 아닙니다.
4. 필요한 프로그램은 작업에 따라 CapCut, FFmpeg, 영상 확인 도구, 사용 허가된 TTS 도구입니다. 이동용 템플릿 설치에는 Python 3가 필요합니다. Hypit CLI를 이용한 URL 분석은 선택 사항이며, 필요하면 [Hypit 원본 저장소](https://github.com/hypit-ai/hypit)의 설치 안내를 따릅니다. 스킬만 복제해도 해당 프로그램이나 계정이 자동 설치되지는 않습니다.

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

스킬 문서는 작업 방식과 기준입니다. **이동용 CapCut 템플릿**은 포함하지만 원본 동영상, 백조 완성 편집본, 유료 서비스 계정, API 키, 게시 권한은 포함하지 않습니다.

## 이동용 CapCut 템플릿

[`templates/glopick_60s/`](templates/glopick_60s/)에 프로젝트 폴더, 교체용 영상 10개, 골드 로고, SRT가 함께 있습니다. 프로젝트 내부의 미디어 경로는 PC마다 달라서 **캡컷을 종료한 뒤** 저장소 루트에서 다음 명령으로 설치하세요.

```powershell
python tools/install_capcut_template.py
```

스크립트는 프로젝트와 로고·영상·SRT를 현재 PC의 CapCut 초안 폴더에 복사하고 미디어 경로를 연결합니다. 같은 이름의 기존 프로젝트는 덮어쓰지 않습니다. 캡컷을 다시 열어 `GloPick 60초 템플릿`을 확인하고 **새 영상 제작 시 프로젝트를 복제해** 회색 컷, 제목, 나레이션 자막을 교체하세요. CapCut 버전이나 설치 상태에 따라 글꼴을 다시 선택해야 할 수 있습니다.

이 템플릿은 파일 구조와 미디어 경로까지 검사했으며, 다른 PC의 CapCut 화면에서 열리는지는 아직 확인하지 못했습니다. 기존 백조 **완성 편집본과 원본 영상**은 이 저장소에 넣지 않았습니다.

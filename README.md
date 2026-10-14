# personal-research-skills

Shared agent skills for research codebases (Claude Code and Codex).

## Install on a computer

```bash
git clone https://github.com/WRafell/personal-research-skills.git ~/agent-skills
mkdir -p ~/.claude/skills ~/.codex/skills
for d in ~/agent-skills/agent-skills/*/; do
  n=$(basename "$d")
  ln -sfn "$d" ~/.claude/skills/"$n"
  ln -sfn "$d" ~/.codex/skills/"$n"
done
```

Update with `git -C ~/agent-skills pull`. The links make each skill available in every repository.

### Windows (Claude Code and Codex on Windows, from WSL)

Windows programs cannot follow WSL links, so copy the skills. Run again after each `git pull`:

```bash
W=/mnt/c/Users/<user>
for d in ~/agent-skills/agent-skills/*/; do
  n=$(basename "$d")
  rsync -a --delete "$d" "$W/.claude/skills/$n/"
  rsync -a --delete "$d" "$W/.codex/skills/$n/"
done
```

The loop replaces only the folders of these skills; other skills (for example Codex `.system`) stay.

## Use in a project

Each project gives its own values (paths, time zone, clusters, environments) in its `AGENTS.md` or
`CLAUDE.md`. Project rules take precedence over these shared skills. See `AGENTS.md` for the skill index.

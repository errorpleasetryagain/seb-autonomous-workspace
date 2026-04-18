# Push All Framework Repos - Mac Terminal Instructions

## IMPORTANT NOTES
- Replace `~/path-to-repo` with the actual path where your repos live (e.g., `~/Passive\ websites/tradepick-framework`)
- Run these commands one at a time and wait for each to complete
- Some repos have uncommitted changes (untracked files) - add them if needed before pushing
- See detailed status below for what's uncommitted in each repo

---

## STEP 1: Fix Git Remotes (if needed)

The following three repos had incorrect remotes pointing to `glwc-framework` instead of their own:
- tradepick-framework
- aibyrole-framework
- remotepivot-framework

These were fixed in the VM. On Mac, verify and fix manually if needed:

### Check current remotes:
```bash
cd ~/path-to-repo
git remote -v
```

### If incorrect, fix with:
```bash
# TRADEPICK
cd ~/path-to-tradepick-framework
git remote set-url origin https://github.com/errorpleasetryagain/tradepick-framework.git

# AIBYROLE
cd ~/path-to-aibyrole-framework
git remote set-url origin https://github.com/errorpleasetryagain/aibyrole-framework.git

# REMOTEPIVOT
cd ~/path-to-remotepivot-framework
git remote set-url origin https://github.com/errorpleasetryagain/remotepivot-framework.git
```

---

## STEP 2: Fetch Latest from All Repos

Run this for each repo to get the latest remote tracking info:

```bash
cd ~/path-to-tradepick-framework && git fetch origin
cd ~/path-to-aibyrole-framework && git fetch origin
cd ~/path-to-remotepivot-framework && git fetch origin
cd ~/path-to-fuel-optimal-framework && git fetch origin
cd ~/path-to-glwc-framework && git fetch origin
cd ~/path-to-liftlab-framework && git fetch origin
```

---

## STEP 3: Handle Uncommitted Changes

**TRADEPICK** has uncommitted files (untracked):
- .gitignore
- README.md
- app/ (directory)
- components/ (directory)
- content/articles/ (directory)

To add and commit these:
```bash
cd ~/path-to-tradepick-framework
git add .
git commit -m "Add framework files and content"
```

**LIFTLAB** has uncommitted files (untracked):
- .gitignore
- README.md
- app/ (directory)
- components/ (directory)
- content/articles/ (directory)

To add and commit these:
```bash
cd ~/path-to-liftlab-framework
git add .
git commit -m "Add framework files and content"
```

**FUEL-OPTIMAL** has 1 uncommitted file:
- content/guides/best-omega3-uk-2026.mdx

To add and commit:
```bash
cd ~/path-to-fuel-optimal-framework
git add content/guides/best-omega3-uk-2026.mdx
git commit -m "Add best-omega3-uk-2026 guide"
```

---

## STEP 4: Push All Repos

```bash
cd ~/path-to-tradepick-framework && git push origin master

cd ~/path-to-aibyrole-framework && git push origin master

cd ~/path-to-remotepivot-framework && git push origin master

cd ~/path-to-fuel-optimal-framework && git push origin master

cd ~/path-to-glwc-framework && git push origin master

cd ~/path-to-liftlab-framework && git push origin main
```

**Note:** liftlab uses `main` branch; the others use `master`.

---

## STEP 5: Fix LiftLab Visibility (Private Repo)

LiftLab should be a private repository. After pushing:

1. Go to: https://github.com/errorpleasetryagain/liftlab-framework/settings
2. Scroll to "Danger Zone"
3. Click "Change repository visibility"
4. Select "Private"
5. Confirm

---

## STEP 6: Fix AIBYROLE Git Corruption

⚠️ **The aibyrole-framework repo has a corrupted git database (bus error on git status).**

The corruption could not be recovered in the VM. On Mac, try:

```bash
cd ~/path-to-aibyrole-framework

# Attempt to repair the repository
git fsck --lost-found

# Try status again
git status

# If still broken, you may need to:
# 1. Back up the content/ directory
# 2. Delete .git directory
# 3. Reinitialize with: git init
# 4. Add remote and restore commit history manually
```

If `git status` works after this, you can proceed with pushing. If it still fails, contact support about repository recovery.

---

## REPO STATUS SUMMARY

| Repo | Branch | Commits Ahead | Uncommitted Changes | Remote Status |
|------|--------|---------------|--------------------|---------------|
| tradepick | master | 1+ | YES (untracked files) | FIXED ✓ |
| aibyrole | master | ? | CORRUPTED | FIXED ✓ |
| remotepivot | master | 1+ | None | FIXED ✓ |
| fuel-optimal | master | 0 | 1 file | Correct ✓ |
| glwc | master | 0 | None | Correct ✓ |
| liftlab | main | 0 | YES (untracked files) | Correct ✓ |

---

## QUICK COPY-PASTE ORDER

If you want to just copy-paste the essentials:

1. Fix remotes (tradepick, aibyrole, remotepivot) - see STEP 1
2. Fetch all - STEP 2
3. Add & commit uncommitted files - STEP 3
4. Push all - STEP 4
5. Make liftlab private - STEP 5
6. Fix aibyrole corruption - STEP 6

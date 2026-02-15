# CHANGELOG — TechQuest Landing Page

All notable changes to the TechQuest landing page.

---

## [2026-02-15] — Co-Builder Pivot + Form Fix

### Changed
- **Hero tagline:** "AI-Powered Project Management" → "Building the PM tool we actually need — together."
- **Hero subtitle:** Updated to community-focused copy targeting operators, PMs, and builders
- **Page title:** Updated to match new co-builder angle
- **Project CTA section:** "One Dynamic PM App to Rule Them All" → "Come Build With Us" — reframed as open build invitation
- **Project CTA button:** "Follow the Build →" → "Join the Build →"
- **Project tag:** "NOW BUILDING" → "OPEN BUILD"
- **Email section header:** "Stay in the Loop" → "Join the Build"
- **Email CTA:** "Get updates as we build..." → "Get early access and help shape what comes next."
- **Email button:** "Notify Me" → "I'm In"
- **Email success message:** Updated to welcome builders

### Fixed
- **Email form broken** — Formspree endpoint `xwpqdrre` was returning 404 (dead/expired)
- **Swapped to FormSubmit.co** — zero-signup service, emails go to `official.techquest.ai@gmail.com`
- Added AJAX submission with loading state ("Sending...") and error handling ("Try Again")
- Added `_captcha=false`, `_template=table` hidden fields for cleaner experience

### Notes
- First submission triggers a confirmation email to `official.techquest.ai@gmail.com` — must be clicked once to activate
- Reported by Rebecca (couldn't submit email, nothing happened)

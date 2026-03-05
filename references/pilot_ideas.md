# Pilot Idea Library

Detailed descriptions of pilot ideas and when to use each based on prospect context.

## Release-Readiness Checklist

**Best for**: Engineering managers, tech leads, release managers
**Stack signals**: CI/CD, deployment pipelines, release processes
**Description**: A focused checklist to verify code is ready for production—covers tests, docs, configs, and rollbacks

**Sample hook**: "Since you're shipping weekly, a release-readiness checklist could cut your rollback rate"

## Incident Handoff / Runbook Capture

**Best for**: SREs, DevOps engineers, platform teams
**Stack signals**: Incident management, on-call, observability tools
**Description**: Document the institutional knowledge around incident response so handoffs are smooth

**Sample hook**: "Saw your post about on-call—capturing runbooks could make your next handoff way easier"

## Repo Readiness / Onboarding Checklist

**Best for**: Engineering managers, team leads, developer experience
**Stack signals**: GitHub, GitLab, codebase, new hire onboarding
**Description**: A checklist to ensure every new repo has what developers need to contribute fast

**Sample hook**: "Since you're growing the team, a repo-readiness checklist could speed up onboarding"

## Data-Quality or Validation Workflow

**Best for**: Data engineers, analysts, QA
**Stack signals**: Data pipelines, ETL, databases, Great Expectations, dbt
**Description**: A workflow to catch bad data before it spreads through your system

**Sample hook**: "Since you're dealing with data pipelines, a validation workflow could catch issues early"

## Migration Readiness Checklist

**Best for**: Technical leads, architects, platform engineers
**Stack signals**: Legacy systems, cloud migration, major refactors
**Description**: A focused checklist to assess readiness before a big migration

**Sample hook**: "A migration-readiness checklist could help you spot gaps before you start"

## Selection Guidance

Pick the **smallest** pilot that connects to their role:

1. Do they own releases? → Release-readiness checklist
2. Do they handle incidents? → Runbook capture
3. Are they bringing on people? → Onboarding checklist
4. Do they work with data? → Validation workflow
5. Are they planning a migration? → Migration readiness

Keep it low-risk and tied to something they already care about.

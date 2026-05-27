/**
 * DevOps Maturity Self-Assessment
 * Swift Tech Co. — https://swifttechco.com
 *
 * Scores DevOps maturity across 7 dimensions (0=basic, 1=developing, 2=advanced).
 */

const QUESTIONS = [
  { id: "cicd",  label: "CI/CD pipeline",           options: ["No CI/CD: manual deploys", "Partial: some automation", "Full CI/CD: auto-deploy on merge"] },
  { id: "iac",   label: "Infrastructure as Code",    options: ["Manual server config", "Partial IaC (some scripts)", "Full IaC (Terraform/Pulumi)"] },
  { id: "mon",   label: "Monitoring & alerting",     options: ["No monitoring", "Basic uptime checks", "Full observability (logs + metrics + traces)"] },
  { id: "dep",   label: "Deployment time",           options: ["> 30 min or manual", "5 to 30 minutes", "< 5 minutes (automated)"] },
  { id: "test",  label: "Automated test coverage",   options: ["No automated tests", "< 50% coverage", "> 80% coverage"] },
  { id: "env",   label: "Environment setup",         options: ["Production only", "Dev + Production", "Dev + Staging + Production"] },
  { id: "dr",    label: "Disaster recovery",         options: ["No plan", "Documented but untested", "Documented + tested regularly"] },
];

/**
 * @param {Object} answers - Maps question id to answer index (0, 1, or 2).
 * @returns {{ score: number, pct: number, level: string, gaps: string[] }}
 */
function calculate(answers) {
  const missing = QUESTIONS.map(q => q.id).filter(id => answers[id] === undefined);
  if (missing.length) throw new Error(`Missing answers for: ${missing.join(", ")}`);

  const score = QUESTIONS.reduce((s, q) => s + (answers[q.id] || 0), 0);
  const pct   = Math.round(score / (QUESTIONS.length * 2) * 100);
  const level = pct <= 25 ? "Basic" : pct <= 50 ? "Developing" : pct <= 75 ? "Advanced" : "Elite";
  const gaps  = QUESTIONS.filter(q => (answers[q.id] || 0) < 2).map(q => q.label);

  return { score, pct, level, gaps };
}

module.exports = { QUESTIONS, calculate };

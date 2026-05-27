#!/usr/bin/env node
/**
 * DevOps Maturity Self-Assessment — CLI
 * Swift Tech Co. — https://swifttechco.com
 */

const { QUESTIONS, calculate } = require("./calculator");
const readline = require("readline");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask = (q) => new Promise(r => rl.question(q, r));

async function interactive() {
  console.log("\nDevOps Maturity Self-Assessment");
  console.log("Swift Tech Co. — https://swifttechco.com");
  console.log("=".repeat(48));
  console.log("Rate your DevOps practices across 7 dimensions.\n");

  const answers = {};
  for (let i = 0; i < QUESTIONS.length; i++) {
    const q = QUESTIONS[i];
    console.log(`${i + 1}. ${q.label}`);
    q.options.forEach((opt, j) => console.log(`   ${j}. ${opt}`));
    const raw = await ask("   Your answer (0/1/2): ");
    answers[q.id] = Math.min(2, Math.max(0, parseInt(raw.trim(), 10) || 0));
    console.log();
  }

  rl.close();

  const result = calculate(answers);
  console.log("=".repeat(48));
  console.log(`Score: ${result.pct} / 100 — ${result.level} DevOps Maturity`);
  if (result.gaps.length) {
    console.log("\nTop areas to improve:");
    result.gaps.slice(0, 4).forEach(g => console.log(`  -> ${g}`));
  }
  console.log("\nGet a DevOps improvement plan: https://swifttechco.com/contact");
}

interactive().catch(e => { console.error(e.message); process.exit(1); });

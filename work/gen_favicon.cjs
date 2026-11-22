// 生成 favicon.svg（定稿 E1：白色几何 D + 底部红/蓝水线双带）。
// 用 .cjs —— package.json 里有 "type": "module"，.js 会被当 ESM。
const fs = require('node:fs');

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Dockyard">
  <defs>
    <linearGradient id="h" x1="0.2" y1="0" x2="0.8" y2="1">
      <stop offset="0" stop-color="#22364a"/><stop offset="0.5" stop-color="#0f1a24"/><stop offset="1" stop-color="#070d13"/>
    </linearGradient>
    <linearGradient id="p" x1="0" y1="0" x2="1" y2="0.4">
      <stop offset="0" stop-color="#a81c26"/><stop offset="0.5" stop-color="#d32a34"/><stop offset="1" stop-color="#a81c26"/>
    </linearGradient>
    <linearGradient id="s" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4a9dd1"/><stop offset="1" stop-color="#19527f"/>
    </linearGradient>
    <linearGradient id="w" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d8eefb"/>
    </linearGradient>
    <clipPath id="c"><rect x="2" y="2" width="44" height="44" rx="11"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect x="2" y="2" width="44" height="44" fill="url(#h)"/>
    <rect x="2" y="30" width="44" height="6.4" fill="url(#p)"/>
    <rect x="2" y="36.4" width="44" height="9.6" fill="url(#s)"/>
    <path d="M16 11 H24 A13 13 0 0 1 24 37 H16 Z M20 15.5 H24 A8.5 8.5 0 0 1 24 32.5 H20 Z"
          fill="url(#w)" fill-rule="evenodd"/>
  </g>
  <rect x="2" y="2" width="44" height="44" rx="11" fill="none" stroke="rgba(255,255,255,0.18)"/>
</svg>
`;

fs.writeFileSync('public/favicon.svg', svg, 'utf8');
console.log('wrote public/favicon.svg', svg.length, 'bytes');

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>XML ID 비교기</title>
  <style>
    textarea {
      width: 48%;
      height: 200px;
      margin: 10px;
      font-family: monospace;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    th, td {
      border: 1px solid #888;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
    td.diff {
      background-color: #ffe0e0;
    }
    td.common {
      background-color: #e0ffe0;
    }
  </style>
</head>
<body>
  <h2>📄 XML ID 비교기 </h2>

  <textarea id="xmlA" placeholder="📥 XML A 입력"></textarea>
  <textarea id="xmlB" placeholder="📥 XML B 입력"></textarea>

  <div id="result">
    <h3>✅ 비교 결과</h3>
    <button type="button" onclick="copyCommonColumn('mappingTable', 0)">공통 Copy</button>
    <table  id="mappingTable">
      <thead>
        <tr>
          <th>ID</th>
          <th>XML A</th>
          <th>XML B</th>
        </tr>
      </thead>
      <tbody id="resultBody"></tbody>
    </table>
  </div>

  <script>
    const xmlAInput = document.getElementById("xmlA");
    const xmlBInput = document.getElementById("xmlB");
    const resultBody = document.getElementById("resultBody");

    const valuesCommon = [];


function parseIds(xmlStr) {
  if (!xmlStr.trim()) return [];

  try {
    // 네임스페이스 접두사 제거 (ex: <w2:column> → <column>)
    const cleanedXmlStr = xmlStr.replace(/<[/]?w2:/g, "<").replace(/<\/w2:/g, "</");

    const parser = new DOMParser();
    const doc = parser.parseFromString(cleanedXmlStr, "application/xml");

    //return Array.from(doc.getElementsByTagName("column"))
    //  .map(el => el.getAttribute("id"))
    //  .filter(Boolean);
    const columnEls = Array.from(doc.getElementsByTagName("column"));
    const keyEls = Array.from(doc.getElementsByTagName("key"));
    //const allEls = [...columnEls, ...keyEls];
    const allEls = mergeUniquePreserveOrder(columnEls, keyEls);

    return allEls
      .map(el => el.getAttribute("id"))
      .filter(Boolean); // null/undefined 제외
  } catch (e) {
    console.error("XML 파싱 오류:", e);
    return [];
  }
}

function mergeUniquePreserveOrder(arr1, arr2) {
  const seen = new Set();
  const merged = [];

  [...arr1, ...arr2].forEach(id => {
    if (!seen.has(id)) {
      seen.add(id);
      merged.push(id);
    }
  });

  return merged;
}

 function updateComparison() {
      const idsA = parseIds(xmlAInput.value);
      const idsB = parseIds(xmlBInput.value);
      //const allIds = Array.from(new Set([...idsA, ...idsB])).sort();
      const allIds = Array.from(new Set([...idsA, ...idsB]));

      resultBody.innerHTML = "";


      allIds.forEach(id => {
        const inA = idsA.includes(id);
        const inB = idsB.includes(id);

       // console.log("allIds id, inA,inB:", id, inA, inB);


        const row = document.createElement("tr");

        const idCell = document.createElement("td");
        idCell.textContent = id;

        const aCell = document.createElement("td");
        const bCell = document.createElement("td");

        aCell.textContent = inA ? "✅" : "";
        bCell.textContent = inB ? "✅" : "";

        if (inA && inB) {
          aCell.classList.add("common");
          bCell.classList.add("common");

          valuesCommon.push(id);
        } else {
          if (!inA) aCell.classList.add("diff");
          if (!inB) bCell.classList.add("diff");
        }

        row.appendChild(idCell);
        row.appendChild(aCell);
        row.appendChild(bCell);

        resultBody.appendChild(row);
      });
    }

function copyCommonColumn(talNm, colIdx) {
  const colIndex = parseInt(colIdx, 10);
  const table = document.getElementById(talNm);
  const rows = table.querySelectorAll("tbody tr");
  const values = [];


  const textToCopy = valuesCommon.join("\n");

  navigator.clipboard.writeText(textToCopy).then(() => {
    alert(`열 ${colIndex} 복사 완료:\n\n` + textToCopy);
  }).catch(err => {
    alert("클립보드 복사 실패: " + err);
  });
}

    xmlAInput.addEventListener("input", updateComparison);
    xmlBInput.addEventListener("input", updateComparison);
  </script>
</body>
</html>

```

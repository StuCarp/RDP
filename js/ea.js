// ea.js - Tree sync script
function highlightTreeItem(guid) {
  try {
    var treeFrame = parent.frames['tree'];
    if (!treeFrame) return;
    var el = treeFrame.document.getElementById(guid);
    if (el) {
      el.scrollIntoView();
      el.style.backgroundColor = '#cceeff';
    }
  } catch (e) {
    console.log('Error highlighting tree item:', e);
  }
}

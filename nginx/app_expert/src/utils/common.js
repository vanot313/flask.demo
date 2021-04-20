export function formatWeight(s) {
  s = s.slice(2, s.length - 2)
  s = s.replace(/\(/g, '').replace(/\)/g, '').replace(/ /g, '')
  const items = s.split(',')
  for (let i = 0; i < items.length; i++) {
    items[i] = items[i].substr(0, 6)
  }
  s = items.concat()
  s = '[' + s.toString() + ']'
  return JSON.parse(s)
}

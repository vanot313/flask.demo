export function moveElement(arr, n) {
  if (Math.abs(n) > arr.length) n = n % arr.length
  return arr.slice(-n).concat(arr.slice(0, -n))
}

export function getWeekDay() {
  let weekDay = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
  weekDay = moveElement(weekDay, 6 - new Date().getDay())
  return weekDay
}

export function formatWeight(s) {
  s = s.slice(2, s.length - 2)
  s = s.replace(/\(/g, '').replace(/\)/g, '').replace(/ /g, '')
  let items = s.split(',')
  for (let i = 0; i < items.length; i++) {
    items[i] = items[i].substr(0, 6)
  }
  s = items.concat()
  s = '[' + s.toString() + ']'
  return JSON.parse(s)
}

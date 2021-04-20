export function loadJs(src) {
  const script = document.createElement('script')
  script.type = 'text/javascript'
  script.src = src
  document.getElementsByTagName('body')[0].appendChild(script)
}

export function asyncLoadJs(src) {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script')
    script.type = 'text/javascript'
    script.onload = () => {
      resolve()
    }
    script.onerror = () => {
      reject()
    }
    script.src = src
    document.getElementsByTagName('body')[0].appendChild(script)
  })
}

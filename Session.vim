let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/code/design-project
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +8 ~/code/design-project/js-scripts/submit.js
badd +91 ~/code/design-project/js-scripts/form.js
badd +1 ~/code/design-project/js-scripts/index.js
badd +27 ~/code/design-project/js-scripts/showRecs.js
badd +55 ~/code/design-project/index.html
badd +11 ~/code/design-project/js-scripts/tabs.js
badd +81 ~/code/design-project/style.css
badd +12 ~/code/design-project/chart.html
badd +1 ~/code/design-project/js-scripts/chart.js
argglobal
%argdel
edit ~/code/design-project/index.html
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
wincmd =
argglobal
balt ~/code/design-project/js-scripts/index.js
let s:l = 55 - ((29 * winheight(0) + 20) / 40)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 55
normal! 08|
wincmd w
argglobal
if bufexists(fnamemodify("~/code/design-project/js-scripts/chart.js", ":p")) | buffer ~/code/design-project/js-scripts/chart.js | else | edit ~/code/design-project/js-scripts/chart.js | endif
if &buftype ==# 'terminal'
  silent file ~/code/design-project/js-scripts/chart.js
endif
balt ~/code/design-project/chart.html
let s:l = 11 - ((10 * winheight(0) + 20) / 40)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 11
normal! 03|
wincmd w
wincmd =
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :

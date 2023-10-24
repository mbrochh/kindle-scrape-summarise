import{o as d,e as k,f as e,d as B,b as w,y,q as m,z as T,_ as z,A as C,B as M,C as H,c as b,a as R,D as A,E as N,G as D,I,J as U,K as E,L,M as j,N as q,O as F,P as O,s as W,Q as Z,R as G,g as l,l as c,t as J,n as g,i as $,S as V,T as P,m as K,U as Q,j as X,V as x,W as Y,X as ee,F as se,Y as te,Z as le,$ as oe,a0 as ae,a1 as ne,a2 as ie,a3 as re}from"./index-5972d117.js";import{N as ce}from"./NoteDisplay-dad763ca.js";import ue from"./DrawingControls-992434d8.js";const de={class:"slidev-icon",viewBox:"0 0 32 32",width:"1.2em",height:"1.2em"},_e=e("path",{fill:"currentColor",d:"M12 10H6.78A11 11 0 0 1 27 16h2A13 13 0 0 0 6 7.68V4H4v8h8zm8 12h5.22A11 11 0 0 1 5 16H3a13 13 0 0 0 23 8.32V28h2v-8h-8z"},null,-1),me=[_e];function pe(i,u){return d(),k("svg",de,me)}const ve={name:"carbon-renew",render:pe},he={class:"slidev-icon",viewBox:"0 0 32 32",width:"1.2em",height:"1.2em"},fe=e("path",{fill:"currentColor",d:"M16 30a14 14 0 1 1 14-14a14 14 0 0 1-14 14Zm0-26a12 12 0 1 0 12 12A12 12 0 0 0 16 4Z"},null,-1),ge=e("path",{fill:"currentColor",d:"M20.59 22L15 16.41V7h2v8.58l5 5.01L20.59 22z"},null,-1),xe=[fe,ge];function we(i,u){return d(),k("svg",he,xe)}const ye={name:"carbon-time",render:we},ke="/kindle-scrape-summarise/assets/logo-title-horizontal-96c3c915.png",Se=B({__name:"NoteStatic",props:{class:{type:String,required:!1}},setup(i){const u=i,v=w(()=>{var o,a,s;return(s=(a=(o=y.value)==null?void 0:o.meta)==null?void 0:a.slide)==null?void 0:s.note}),h=w(()=>{var o,a,s;return(s=(a=(o=y.value)==null?void 0:o.meta)==null?void 0:a.slide)==null?void 0:s.noteHTML});return(o,a)=>(d(),m(ce,{class:T(u.class),note:v.value,"note-html":h.value},null,8,["class","note","note-html"]))}}),Ce=z(Se,[["__file","/Users/martin/Projects/pugs/presentations/kindle-scrape-summarise/slidev/node_modules/@slidev/client/internals/NoteStatic.vue"]]),p=i=>(ie("data-v-574fd206"),i=i(),re(),i),be={class:"bg-main h-full slidev-presenter"},Ne={class:"grid-container"},$e={class:"grid-section top flex"},Ve=p(()=>e("img",{src:ke,class:"ml-2 my-auto h-10 py-1 lg:h-14 lg:py-2",style:{height:"3.5rem"},alt:"Slidev logo"},null,-1)),Pe=p(()=>e("div",{class:"flex-auto"},null,-1)),Be={class:"text-2xl pl-2 pr-6 my-auto tabular-nums"},Te=p(()=>e("div",{class:"context"}," current ",-1)),ze=p(()=>e("div",{class:"context"}," next ",-1)),Me={class:"grid-section note overflow-auto"},He={class:"grid-section bottom"},Re={class:"progress-bar"},Ae=B({__name:"Presenter",setup(i){const u=C();M(),H(u);const v=b.titleTemplate.replace("%s",b.title||"Slidev");R({title:`Presenter - ${v}`});const{timer:h,resetTimer:o}=A(),a=C([]),s=w(()=>N.value<D.value?{route:y.value,clicks:N.value+1}:I.value?{route:U.value,clicks:0}:null);return E(),L(()=>{const S=u.value.querySelector("#slide-content"),n=j(q()),f=F();O(()=>{if(!f.value||Z.value||!G.value)return;const r=S.getBoundingClientRect(),t=(n.x-r.left)/r.width*100,_=(n.y-r.top)/r.height*100;if(!(t<0||t>100||_<0||_>100))return{x:t,y:_}},r=>{W.cursor=r})}),(S,n)=>{const f=ye,r=ve;return d(),k(se,null,[e("div",be,[e("div",Ne,[e("div",$e,[Ve,Pe,e("div",{class:"timer-btn my-auto relative w-22px h-22px cursor-pointer text-lg",opacity:"50 hover:100",onClick:n[0]||(n[0]=(...t)=>l(o)&&l(o)(...t))},[c(f,{class:"absolute"}),c(r,{class:"absolute opacity-0"})]),e("div",Be,J(l(h)),1)]),e("div",{ref_key:"main",ref:u,class:"relative grid-section main flex flex-col p-2 lg:p-4",style:g(l($))},[c(P,{key:"main",class:"h-full w-full"},{default:V(()=>[c(te,{"render-context":"presenter"})]),_:1}),Te],4),e("div",{class:"relative grid-section next flex flex-col p-2 lg:p-4",style:g(l($))},[s.value?(d(),m(P,{key:"next",class:"h-full w-full"},{default:V(()=>{var t;return[c(l(oe),{is:(t=s.value.route)==null?void 0:t.component,"clicks-elements":a.value,"onUpdate:clicksElements":n[1]||(n[1]=_=>a.value=_),clicks:s.value.clicks,"clicks-disabled":!1,class:T(l(le)(s.value.route)),route:s.value.route,"render-context":"previewNext"},null,8,["is","clicks-elements","clicks","class","route"])]}),_:1})):K("v-if",!0),ze],4),e("div",Me,[(d(),m(Ce,{key:2,class:"w-full max-w-full h-full overflow-auto p-2 lg:p-4"}))]),e("div",He,[c(ae,{persist:!0})]),(d(),m(ue,{key:0}))]),e("div",Re,[e("div",{class:"progress h-2px bg-primary transition-all",style:g({width:`${(l(Q)-1)/(l(X)-1)*100}%`})},null,4)])]),c(ne),c(ee,{modelValue:l(x),"onUpdate:modelValue":n[2]||(n[2]=t=>Y(x)?x.value=t:null)},null,8,["modelValue"])],64)}}});const Ee=z(Ae,[["__scopeId","data-v-574fd206"],["__file","/Users/martin/Projects/pugs/presentations/kindle-scrape-summarise/slidev/node_modules/@slidev/client/internals/Presenter.vue"]]);export{Ee as default};

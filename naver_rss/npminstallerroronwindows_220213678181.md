##npm install error on windows
						<div id="postViewArea">						<div id="postViewArea">						<div id="post-view220213678181" class="post-view pcol2 _param(1) _postViewArea220213678181">						<div id="post-view220213678181" class="post-view pcol2 _param(1) _postViewArea220213678181">							<p>[Error발생 ]</p><p>- 기본 npm은 잘 설치됬으나 install시 안되서 <img src="http://static.se2.naver.com/static/full/20130612/emoticon/2_05.gif" onload="setTimeout('utility.resizeImageWithId(\'static/full/20130612/emoticon/2_05.gif\')',200)" style="cursor: pointer;" id="static/full/20130612/emoticon/2_05.gif" onclick="popview(this, '90000003_000000000000003345C21065')" alt="">삽질</p><p><br /></p><p>D:\workspace_node&gt;npm install --global javascripting<br />npm ERR! Error: <strong>UNABLE_TO_VERIFY_LEAF_SIGNATURE</strong><br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at SecurePair.&lt;anonymous&gt; (tls.js:1381:32)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at SecurePair.emit (events.js:92:17)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at SecurePair.maybeInitFinished (tls.js:980:10)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at CleartextStream.read [as _read] (tls.js:472:13)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at CleartextStream.Readable.read (_stream_readable.js:341:10)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at EncryptedStream.write [as _write] (tls.js:369:25)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at doWrite (_stream_writable.js:226:10)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at writeOrBuffer (_stream_writable.js:216:5)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at EncryptedStream.Writable.write (_stream_writable.js:183:11)<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; at write (_stream_readable.js:602:24)<br />npm ERR! If you need help, you may report this *entire* log,<br />npm ERR! including the npm and node versions, at:<br />npm ERR!&nbsp;&nbsp;&nbsp;&nbsp; &lt;<a href="http://github.com/npm/npm/issues" target="_blank" class="con_link">http://github.com/npm/npm/issues</a>&gt;</p><p>npm ERR! System Windows_NT 6.2.9200</p><p>....<br /></p><p><br /></p><p>[해결방법]</p><p>C:\Users\MyId\.npmrc</p><p>windows 사용자 개인폴더에 .npmrc파일 내용을 아래와 같이&nbsp;설정</p><p><br /></p><p>registry = <a href="http://registry.npmjs.org/" target="_blank" class="con_link">http://registry.npmjs.org/</a><br />strict-ssl=false<br />ca=</p><p><br /></p><p>[해결 후]</p><p>D:\workspace_node&gt;npm install --global javascripting<br />C:\Users\MyId\AppData\Roaming\npm\javascripting -&gt; C:\Users\MyId\AppData\Roa<br />ming\npm\node_modules\javascripting\index.js<br /><a href="mailto:javascripting@1.8.0" target="_blank" class="con_link">javascripting@1.8.0</a> C:\Users\MyId\AppData\Roaming\npm\node_modules\javascripti<br />ng<br />├── <a href="mailto:adventure@2.8.0" target="_blank" class="con_link">adventure@2.8.0</a> (<a href="mailto:inherits@2.0.1" target="_blank" class="con_link">inherits@2.0.1</a>, <a href="mailto:x256@0.0.2" target="_blank" class="con_link">x256@0.0.2</a>, <a href="mailto:minimist@0.2.0" target="_blank" class="con_link">minimist@0.2.0</a>, <a href="mailto:mkdirp@0.5.0" target="_blank" class="con_link">mkdirp@0.5.0</a><br />, <a href="mailto:split@0.3.2" target="_blank" class="con_link">split@0.3.2</a>, <a href="mailto:through2@0.5.1" target="_blank" class="con_link">through2@0.5.1</a>, <a href="mailto:terminal-menu@0.2.0" target="_blank" class="con_link">terminal-menu@0.2.0</a>)<br />└── <a href="mailto:cli-md@0.1.0" target="_blank" class="con_link">cli-md@0.1.0</a> (<a href="mailto:marked@0.3.2" target="_blank" class="con_link">marked@0.3.2</a>, <a href="mailto:chalk@0.5.1" target="_blank" class="con_link">chalk@0.5.1</a>, <a href="mailto:concat-stream@1.4.7" target="_blank" class="con_link">concat-stream@1.4.7</a>, <a href="mailto:cardinal@0" target="_blank" class="con_link">cardinal@0</a>.<br />4.4)</p><p><br /></p>						</div>						</div>
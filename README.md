<div align="center">

   <h1>Safe Delete</h1>
    
</div>

<div align="center">

   <h2>Why?</h2>
   Did this project come through my studies on where the files go when we exclude them?<br>
   And that is why I created this little project.
   <p>
    Based on <a href="https://www.youtube.com/playlist?list=PLUKKAhdBKPE__OmJC0QE__aY47yUops5l">Protegendo seus dados</a> playlist by <a href="https://www.youtube.com/@coachdeosasco">Coach de Osasco</a>. I opened my eyes to this topic, and plunged into my studies.
   </p>


</div>


<div align="center">

   <h2>How?</h2>
    Studying about this topic of erasing files, I saw that when erasing the files, they are not completely erased, only the notes are deleted and the space that previously occupied is shown as free, but the raw data is still there, just waiting to be overwritten by future data. With this, using forensic tools it is possible to read this raw data in search of bytes patterns used by the files, thus being able to restore it, completely or restore fragments if a part of the original file has been spared by another file.

</div>

<div align="center">

   <h2>So how to effectively delete files?</h2>
    In short. We apply the Gutmann method to a file on a hard disk, we overwrite the file's bytes 35 times, and then we delete it.
    <p>
    It is worth mentioning that Gutmann's method is only effective on HARD DRIVES, because on a hard drive, repeatedly overwriting the bytes of a file wears out the storage cell, thus causing the "deletion of files". On Flash drives such as SSDs, pendrives or SD cards, the way data is stored is different, and the wear of the storage cell does not occur as it does on a hard drive, and therefore the file is not effectively deleted.
    </p>

</div>

<div align="center">

   <h2>How to use the script?</h2>

   <div align="left">
      <h4>⚠️CAUTIONS⚠️</h4>
   
   * This script is recommended for HARD DRIVES<br>
   * Once you delete the file, it is IMPOSSIBLE to recover it
   </div>
   
   <br>

   <p>
      To use the secure delete script I created, place all the files you want to delete in the same folder where the script is, then run the script.
   </p>
    
</div>



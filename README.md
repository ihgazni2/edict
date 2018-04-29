# edict

>__handle dict, flatten__

# install 

>__pip3 install edict__

-----------------------------------------------------------------------

## _class_ Edict
-----------------------------------------------------------------------
>├──0. [\_\_init\_\_](edict/Images/__init__.0.png) <br>
├──1. [\_\_repr\_\_](edict/Images/__repr__.0.png)  <br>
├──2. [keypaths\<0\>](edict/Images/keypaths.0.png)  <br>
├──2. [keypaths\<1\>](edict/Images/keypaths.1.png)  <br>
├──2. [keypaths\<2\>](edict/Images/keypaths.2.png)  <br>
├──2. [keys\<0\>](edict/Images/keys.0.png)  <br>
├──2. [keys\<1\>](edict/Images/keys.1.png)  <br>
├──2. [values\<0\>](edict/Images/values.0.png)  <br>
├──2. [values\<1\>](edict/Images/values.1.png)  <br>
├──2. [values\<2\>](edict/Images/values.2.png)  <br>
├──2. [values\<3\>](edict/Images/values.3.png)  <br>
├──2. [ktree](edict/Images/ktree.0.png)  <br>
├──3. [\_\_getitem\_\_](edict/Images/__getitem__.0.png)  <br>
├──4. [\_\_setitem\_\_](edict/Images/__setitem__.0.png)  <br>
├──5. [\_\_delitem\_\_](edict/Images/__delitem__.0.png)  <br>
├──6. [include_pathlist](edict/Images/include_pathlist.0.png)  <br>
├──7. [pathlists](edict/Images/pathlists.0.png)  <br>
├──8. [bracket_lists](edict/Images/bracket_lists.0.png)  <br>
├──9. [keys_via_value\<0\>](edict/Images/keys_via_value.0.png)  <br>
├──9. [keys_via_value\<1\>](edict/Images/keys_via_value.1.png)  <br>
├──9. [pathlists_via_value\<0\>](edict/Images/keys_via_value.0.png)  <br>
├──9. [pathlists_via_value\<1\>](edict/Images/keys_via_value.1.png)  <br>
├──9. [bracket_lists_via_value\<0\>](edict/Images/bracket_lists_via_value.0.png)  <br>
├──9. [bracket_lists_via_value\<1\>](edict/Images/bracket_lists_via_value.1.png)  <br>
├──10. [vksdesc](edict/Images/vksdesc.0.png)  <br>
├──11. [uniqualize](edict/Images/uniqualize.0.png)  <br>
├──12. [extend\<0\>](edict/Images/extend.0.png)  <br>
├──12. [extend\<1\>](edict/Images/extend.1.png)  <br>
├──13. [update_intersection](edict/Images/update_intersection.0.png)  <br>
├──14. [update\<0\>](edict/Images/update.0.png)  <br>
├──15. [update\<1\>](edict/Images/update.1.png)  <br>
├──16. [union](edict/Images/union.0.png)  <br>
├──17. [intersection](edict/Images/intersection.0.png)  <br>
├──18. [diff](edict/Images/diff.0.png)  <br>
├──19. [complement](edict/Images/complement.0.png)  <br>
├──20. [comprise](edict/Images/comprise.0.png)  <br>
├──21. [tlist](edict/Images/tlist.0.png)  <br>
├──22. [setdefault](edict/Images/setdefault.0.png)  <br>
├──23. [rvwfs](edict/Images/rvwfs.0.png)  <br>
├──24. [rvdfs](edict/Images/rvdfs.0.png)  <br>
├──25. [rvmat](edict/Images/rvmat.0.png)  <br>
├──26. [kwfs](edict/Images/wfs.0.png)  <br>
├──27. [vwfs](edict/Images/wfs.0.png)  <br>
├──28. [wfses](edict/Images/wfs.0.png)  <br>
├──29. [kdfs](edict/Images/dfs.0.png)  <br>
├──30. [vdfs](edict/Images/dfs.0.png)  <br>
├──31. [dfses](edict/Images/dfs.0.png)  <br>
├──32. [kdmat](edict/Images/kdmat.0.png)  <br>
├──33. [vndmat](edict/Images/vndmat.0.png)  <br>
├──34. [ktvndmats](edict/Images/ktvndmats.0.png)  <br>
├──35. [kpmat](edict/Images/kpmat.0.png)  <br>
├──36. [vnest](edict/Images/vnest.0.png)  <br>
├──37. [ktree_vnest](edict/Images/ktree_vnest.0.png)  <br>
├──38. [klist](edict/Images/klist.0.png)  <br>
├──39. [vlist](edict/Images/vlist.0.png)  <br>
├──40. [kvlists](edict/Images/kvlists.0.png)  <br>
├──41. [contains\<0\>](edict/Images/contains.0.png)  <br>
├──42. [contains\<1\>](edict/Images/contains.1.png)  <br>
├──43. [count\<0\>](edict/Images/count.0.png)  <br>
├──44. [count\<1\>](edict/Images/count.1.png)  <br>
├──45. [depth](edict/Images/depth.0.png)  <br>
├──46. [total](edict/Images/depth.0.png)  <br>
├──47. [maxLevelWidth](edict/Images/depth.0.png)  <br>
├──48. [flatWidth](edict/Images/depth.0.png)  <br>
├──49. [tree\<0\>](edict/Images/tree.0.png)  <br>
├──50. [tree\<1\>](edict/Images/tree.1.png)  <br>
├──51. [cond_select_key\<0\>](edict/Images/cond_select_key.0.png)  <br>
├──52. [cond_select_key\<1\>](edict/Images/cond_select_key.1.png)  <br>
├──53. [cond_select_key\<2\>](edict/Images/cond_select_key.2.png)  <br>
├──54. [cond_select_leaf_value\<0\>](edict/Images/cond_select_leaf_value.0.png)  <br>
├──55. [cond_select_leaf_value\<1\>](edict/Images/cond_select_leaf_value.1.png)  <br>
├──56. [cond_select_keypath\<0\>](edict/Images/cond_select_keypath.0.png)  <br>
├──57. [cond_select_keypath\<1\>](edict/Images/cond_select_keypath.1.png)  <br>
├──58. [ancestor_keypaths\<0\>](edict/Images/ancestors.0.png)  <br>
├──59. [ancestor_keypaths\<1\>](edict/Images/ancestors.1.png)  <br>
├──60. [ancestors\<0\>](edict/Images/ancestors.0.png)  <br>
├──61. [ancestors\<1\>](edict/Images/ancestors.1.png)  <br>
├──62. [parent_keypath\<0\>](edict/Images/parent.0.png)  <br>
├──63. [parent_keypath\<1\>](edict/Images/parent.1.png)  <br>
├──64. [parent\<0\>](edict/Images/parent.0.png)  <br>
├──65. [parent\<1\>](edict/Images/parent.1.png)  <br>
├──66. [descendant_keypaths\<0\>](edict/Images/descendants.0.png)  <br>
├──67. [descendant_keypaths\<1\>](edict/Images/descendants.1.png)  <br>
├──68. [descendants\<0\>](edict/Images/descendants.0.png)  <br>
├──69. [descendants\<1\>](edict/Images/descendants.1.png)  <br>
├──  . **_From py3.6, the dict is ordered, try below in 3.6+_**<br>
├──70. [prevSibPath\<0\>](edict/Images/lsib.0.png)  <br>
├──71. [prevSibPath\<1\>](edict/Images/lsib.1.png)  <br>
├──72. [prevSibling\<0\>](edict/Images/lsib.0.png)  <br>
├──73. [prevSibling\<1\>](edict/Images/lsib.1.png)  <br>
├──74. [lsib_path\<0\>](edict/Images/lsib.0.png)  <br>
├──75. [lsib_path\<1\>](edict/Images/lsib.1.png)  <br>
├──76. [lsib\<0\>](edict/Images/lsib.0.png)  <br>
├──77. [lsib\<1\>](edict/Images/lsib.1.png)  <br>
├──42. [nextSibPath\<0\>](edict/Images/nextSibPath.0.png)  <br>
├──41. [nextSibPath\<1\>](edict/Images/nextSibPath.1.png)  <br>
├──42. [nextSibling\<0\>](edict/Images/nextSibling.0.png)  <br>
├──42. [nextSibling\<1\>](edict/Images/nextSibling.1.png)  <br>
├──41. [rsib_path\<0\>](edict/Images/rsib.0.png)  <br>
├──42. [rsib_path\<1\>](edict/Images/rsib.1.png)  <br>
├──41. [rsib\<0\>](edict/Images/rsib.0.png)  <br>
├──42. [rsib\<1\>](edict/Images/rsib.1.png)  <br>
├──41. [lcin\<0\>](edict/Images/lcin.0.png)  <br>
├──42. [lcin\<1\>](edict/Images/lcin.1.png)  <br>
├──41. [rcin\<0\>](edict/Images/rcin.0.png)  <br>
├──42. [rcin\<1\>](edict/Images/rcin.1.png)  <br>
├──41. [sons\<0\>](edict/Images/sons.0.png)  <br>
├──42. [sons\<1\>](edict/Images/sons.1.png)  <br>
├──42. [sibs\<0\>](edict/Images/sibs.0.png)  <br>
├──41. [sibs\<1\>](edict/Images/sibs.1.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>
├──41. [](edict/Images/.0.png)  <br>
├──42. [](edict/Images/.0.png)  <br>

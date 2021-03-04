public class CollisionDetection : MonoBehavior
{
private void OnTriggerEnter2D(Collider2D collision)
    {
    //SkorArea isimli bolgeye kus carptigi zaman ScoreUpdater fonksiyonu devreye girerek skoru arttirir.
        if (collision.gameObject.name == "ScoreArea")
        {
            //Skor arttiran fonks.
            ScoreUpdater();
        }
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
    //DeathArea etiketli bolgeye kus carptigi zaman oyunu durdurur ve olum ekranini acar.
        if (collision.gameObject.tag == "DeathArea")
        {
        //Oyunun baslayip baslamadigini belirtir
            gameStarted = false;
        //Oyun icindeki zamani durdurur.
            Time.timeScale = 0;
        //Olum ekranini aktif eder.
            DeathScreen.SetActive(true);
        }
    }
}
// DAHA FAZLA BILGI ICIN UNITY DOCUMENTS`I ZIYARET EDEBILIRSINIZ//
//https://docs.unity3d.com/ScriptReference/Collider2D.OnCollisionEnter2D.html//

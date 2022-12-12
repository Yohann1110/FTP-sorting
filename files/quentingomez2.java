import java.util.Scanner;

public class quentingomez2 {

	public static void main(String[] args) {
		int classeSalaire, empl; 
		double salaire=0, augmentation=0, annee=0, total=0, moy=0;
		Scanner scan = new Scanner(System.in);
		System.out.println("Entrer le nombre d'employés");
		empl= scan.nextInt();
		for(int i=0; i<empl; ++i) {
			System.out.println("Enter votre classe de salaire (15, 16 ou 17) : ");
			classeSalaire = scan.nextInt();
			System.out.println("Entrer votre nombre d'année(s) d'expérience : ");
			annee = scan.nextDouble();
			if(annee>20) {
				annee=20;
			}
			switch (classeSalaire) {
				case 15: 
					salaire=5675.10;
					augmentation=113.502;
					break;
				case 16:
					salaire=5410.00;
					augmentation=108.2;
					break;
				case 17:
					salaire=5157.25;
					augmentation=103.145;
					break;
				default :
					salaire=0.0;
					augmentation=0.0;
					
			}
			augmentation = augmentation * annee;
			salaire += augmentation;
			total+=salaire;
		}
		moy=total/empl;		
		System.out.println("Total des salaires : " + total);
		System.out.println("Salaire moyen de l'équipe : " + moy);
		scan.close();
	}

}

import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-nivelDeEnsino',
  templateUrl: './nivelDeEnsino.component.html',
  styleUrls: ['./nivelDeEnsino.component.css']
})
export class NivelDeEnsinoComponent implements OnInit {
  
  EscolaList:any=[];
  nivelDeEnsino: any;

  constructor(private service:SharedService, private route: ActivatedRoute, private router:Router) { 
    this.route.params.subscribe(params => this.nivelDeEnsino = params['nivel']);
    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
  }

  ngOnInit(): void {
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
      this.EscolaList=this.EscolaList?.results;
      this.EscolaList=this.getSchoolsByNivel(this.nivelDeEnsino);
    });
  }

  detail(dataItem: any): void {
    this.router.navigate(['detail', dataItem.cep])
    this.service.selectedSchool = dataItem;
  }

  getSchoolsByNivel(nivel: any) {
    if (nivel == "Pré-alfabetização") {
      return this.EscolaList.filter((escola: any) => escola.preAlfa === true);
    }
    else if (nivel == "EnsinoFundamental") {
      return this.EscolaList.filter((escola: any) => escola.ensinoFundamental === true);
    }
    else if (nivel == "EnsinoMédio") {
      return this.EscolaList.filter((escola: any) => escola.ensinoMedio === true);
    }
    return this.EscolaList;
  }
}
